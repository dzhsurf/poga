#include "poga_manager.hpp"

namespace poga {

PogaManager::PogaManager() {}

PogaManager& PogaManager::get_instance() {
    static PogaManager g_inst;
    return g_inst;
}

PogaManager::~PogaManager() {
    //
}

void PogaManager::set_node_context(const PGNode& node, const py::object& obj) {
    if (obj.is_none()) {
        this->_node_context_map.erase(node.get());
    } else {
        this->_node_context_map[node.get()] = obj;
    }
}

py::object PogaManager::get_node_context(const PGNode& node) {
    auto iter = this->_node_context_map.find(node.get());
    if (iter != this->_node_context_map.end()) {
        return iter->second;
    }
    return py::object(py::none());
}

void PogaManager::update_measure_method(const PGNode& node,
                                        const py::function& func) {
    if (func.is_none()) {
        this->_node_measure_func_map.erase(node.get());
    } else {
        this->_node_measure_func_map[node.get()] = func;
    }
}

py::function PogaManager::get_measure_method_by_node(YGNodeRef node) {
    auto iter = this->_node_measure_func_map.find(node);
    if (iter != this->_node_measure_func_map.end()) {
        return iter->second;
    }
    return py::function();
}

YGSize PogaManager::poga_measure_method(YGNodeRef node,
                                        float width,
                                        YGMeasureMode width_mode,
                                        float height,
                                        YGMeasureMode height_mode) {
    py::function func =
        PogaManager::get_instance().get_measure_method_by_node(node);
    if (func.is_none()) {
        return YGSize();
    }

    py::object val = func(PGNode(node), width, width_mode, height, height_mode);
    return val.cast<YGSize>();
}

void PogaManager::release_node_resources(const PGNode& node) {
    this->set_node_context(node, py::object(py::none()));
    this->update_measure_method(node, py::function());
}

};  // namespace poga