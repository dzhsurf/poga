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

void PogaManager::update_baseline_method(const PGNode& node,
                                         const py::function& func) {
    if (func.is_none()) {
        this->_node_baseline_func_map.erase(node.get());
    } else {
        this->_node_baseline_func_map[node.get()] = func;
    }
}

void PogaManager::update_config_logger_method(const PGConfig& config,
                                              const py::function& func) {
    if (func.is_none()) {
        this->_config_logger_func_map.erase(config.get());
    } else {
        this->_config_logger_func_map[config.get()] = func;
    }
}

void PogaManager::update_config_clone_node_method(const PGConfig& config,
                                                  const py::function& func) {
    if (func.is_none()) {
        this->_config_clone_node_func_map.erase(config.get());
    } else {
        this->_config_clone_node_func_map[config.get()] = func;
    }
}

py::function PogaManager::get_measure_method_by_node(YGNodeRef node) {
    auto iter = this->_node_measure_func_map.find(node);
    if (iter != this->_node_measure_func_map.end()) {
        return iter->second;
    }
    return py::function();
}

py::function PogaManager::get_baseline_method_by_node(YGNodeRef node) {
    auto iter = this->_node_baseline_func_map.find(node);
    if (iter != this->_node_baseline_func_map.end()) {
        return iter->second;
    }
    return py::function();
}

py::function PogaManager::get_config_logger_method_by_config(
    YGConfigRef config) {
    auto iter = this->_config_logger_func_map.find(config);
    if (iter != this->_config_logger_func_map.end()) {
        return iter->second;
    }
    return py::function();
}
py::function PogaManager::get_config_clone_node_method_by_config(
    YGConfigRef config) {
    auto iter = this->_config_clone_node_func_map.find(config);
    if (iter != this->_config_clone_node_func_map.end()) {
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

float PogaManager::poga_baseline_method(YGNodeRef node,
                                        float width,
                                        float height) {
    py::function func =
        PogaManager::get_instance().get_baseline_method_by_node(node);
    if (func.is_none()) {
        return 0.0f;
    }
    py::object val = func(PGNode(node), width, height);
    return val.cast<float>();
}

int PogaManager::poga_config_logger_method(YGConfigRef config,
                                           YGNodeRef node,
                                           YGLogLevel level,
                                           const char* format,
                                           va_list args) {
    py::function func =
        PogaManager::get_instance().get_config_logger_method_by_config(config);
    if (func.is_none()) {
        return 0;
    }
    py::object val =
        func(PGConfig(config), PGNode(node), level, std::string(format), args);
    return val.cast<int>();
}

YGNodeRef PogaManager::poga_config_clone_node_method(YGNodeRef oldNode,
                                                     YGNodeRef owner,
                                                     int childIndex) {
    // TODO: how to get the correct YGConfigRef ???
    py::function func = poga::PogaManager::get_instance()
                            .get_config_clone_node_method_by_config(nullptr);
    if (func.is_none()) {
        return 0;
    }
    py::object val = func(PGNode(oldNode), PGNode(owner), childIndex);
    return val.cast<PGNode>().get();
}

void PogaManager::release_node_resources(const PGNode& node) {
    this->set_node_context(node, py::object(py::none()));
    this->update_measure_method(node, py::function());
    this->update_baseline_method(node, py::function());
}

void PogaManager::release_config_resources(const PGConfig& config) {
    this->update_config_logger_method(config, py::function());
}

};  // namespace poga