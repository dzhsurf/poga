#ifndef _POGA_MANAGER_H_
#define _POGA_MANAGER_H_
#endif

#include <Yoga.h>
#include <pybind11/pybind11.h>
#include <map>

namespace py = pybind11;
namespace poga {

template <class T>
class ptr_wrapper {
   public:
    ptr_wrapper() : ptr(nullptr) {}
    ptr_wrapper(T* ptr) : ptr(ptr) {}
    ptr_wrapper(const ptr_wrapper& other) : ptr(other.ptr) {}
    T& operator*() const { return *ptr; }
    T* operator->() const { return ptr; }
    T* get() const { return ptr; }
    void destroy() { delete ptr; }
    T& operator[](std::size_t idx) const { return ptr[idx]; }

   private:
    T* ptr;
};

typedef ptr_wrapper<YGNode> PGNode;
typedef ptr_wrapper<YGConfig> PGConfig;

class PogaManager {
   public:
    static PogaManager& get_instance();
    virtual ~PogaManager();
    PogaManager(const PogaManager& other) = delete;

    void set_node_context(const PGNode& node, const py::object& obj);
    py::object get_node_context(const PGNode& node);

    void update_measure_method(const PGNode& node, const py::function& func);

    void release_node_resources(const PGNode& node);

    // YGMeasureFunc callback
    static YGSize poga_measure_method(YGNodeRef node,
                                      float width,
                                      YGMeasureMode width_mode,
                                      float height,
                                      YGMeasureMode height_mode);

   private:
    PogaManager();

    py::function get_measure_method_by_node(YGNodeRef node);

    std::map<YGNodeRef, py::object> _node_context_map;
    std::map<YGNodeRef, py::function> _node_measure_func_map;
};

}  // namespace poga
