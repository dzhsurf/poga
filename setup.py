# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poga']

package_data = \
{'': ['*'],
 'poga': ['capi/*',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/BitUtils.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/CompactValue.h',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.cpp',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/Utils.h',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.cpp',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGConfig.h',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.cpp',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGEnums.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGFloatOptional.h',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.cpp',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGLayout.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGMacros.h',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.cpp',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNode.h',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.cpp',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGNodePrint.h',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.cpp',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGStyle.h',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.cpp',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/YGValue.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga-internal.h',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.cpp',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/Yoga.h',
          'deps/yoga/event/*',
          'deps/yoga/internal/*',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.cpp',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h',
          'deps/yoga/log.h']}

setup_kwargs = {
    'name': 'poga',
    'version': '0.1.12',
    'description': 'Python bindings for YogaLayout',
    'long_description': "Poga\n====\n\n [![Docs](https://img.shields.io/badge/docs-latest-informational)](https://dzhsurf.github.io/poga/) \n\n\n\nIntroduction\n-----------------\n\nPoga is a Python binding for YogaLayout.\n\nIt provides Python API for YogaLayout. And a high-level interface PogaLayout.\n\nYogaLayout: https://yogalayout.com/\n\n\n\nInstall\n-------\n\n```shell\n    # Python version requires >= 3.7\n    pip install poga\n```\n\n\n\nQuickstart\n----------\n\nUse high-level interface PogaLayout\n\nMore details you can refer to the PGLayout of the pydui-gtk project below.\n\nhttps://github.com/dzhsurf/pydui\n\n```python\n    from poga import PogaLayout\n\n    def main():\n        layout = PogaLayout()\n        layout.flex_direction = YGFlexDirection.FlexStart\n        # ...\n        layout.apply_layout()\n```\n\nUse Binding CAPI directily\n\n```python\n    from poga.libpoga_capi import *\n\n    def main():\n        node = YGNodeNew()\n        YGNodeSetNodeType(node, YGNodeType.Default)\n        YGNodeFree(node)\n```\n\n\n\nBuilding\n--------\n\nSince there's a need for a cpp compiler to build the python extension module, you should install the build-essential tools before you build the package. \n\n* Windows: `VS16 - VS2019 Build Tools`\n\n* MacOS: `XCode Command Line Tools`\n\n* Linux (Ubuntu):  `build-essential`\n\n```shell\n# checkout the code and enter the diretory\nconda env create -f conda-env.yaml # setup the py env. highly recommended.\nconda activate poga\n# or you can just install the dependencies by poetry. \npoetry install\n# after finish setup the environment. go to install the package.\npip install -e . # install package\ncd src && pip install -e . # enter the src dictory use the setuptools to build the libpoga_capi module\n# now, all done. run the sample code \npython example/main.py\n```\n\n\n\nBenchmark\n---------\n\n```shell\nkernprof -l benchmark.py\npython -m line_profiler benchmark.py.lprof\n```\n\nMacBook Pro (15-inch, 2016)\n\n* Processor 2.7GHz Quad-core Intel Core i7\n* Memory 16GB 2133 MHz LPDDR3\n\n\n\n```\nTimer unit: 1e-06 s\n\nTotal time: 0.000141 s\nFile: benchmark.py\nFunction: stack_with_flex at line 14\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n    14                                           @profile\n    15                                           def stack_with_flex():\n    16         1         20.0     20.0     14.2      root = YGNodeNew()\n    17         1         10.0     10.0      7.1      YGNodeStyleSetWidth(root, 100)\n    18         1          3.0      3.0      2.1      YGNodeStyleSetHeight(root, 100)\n    19        11         10.0      0.9      7.1      for i in range(10):\n    20        10         23.0      2.3     16.3          child = YGNodeNew()\n    21        10         12.0      1.2      8.5          YGNodeStyleSetFlex(child, i)\n    22        10         16.0      1.6     11.3          YGNodeInsertChild(root, child, 0)\n    23\n    24         1         37.0     37.0     26.2      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)\n    25         1         10.0     10.0      7.1      YGNodeFreeRecursive(root)\n\nTotal time: 0.000169 s\nFile: benchmark.py\nFunction: align_stretch_in_undefined_axis at line 28\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n    28                                           @profile\n    29                                           def align_stretch_in_undefined_axis():\n    30         1          2.0      2.0      1.2      root = YGNodeNew()\n    31        11          6.0      0.5      3.6      for i in range(10):\n    32        10         14.0      1.4      8.3          child = YGNodeNew()\n    33        10         10.0      1.0      5.9          YGNodeStyleSetHeight(child, 20)\n    34        10         12.0      1.2      7.1          YGNodeSetMeasureFunc(child, measure_fn)\n    35        10         12.0      1.2      7.1          YGNodeInsertChild(root, child, 0)\n    36\n    37         1        110.0    110.0     65.1      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)\n    38         1          3.0      3.0      1.8      YGNodeFreeRecursive(root)\n\nTotal time: 0.001685 s\nFile: benchmark.py\nFunction: nested_flex at line 41\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n==============================================================\n    41                                           @profile\n    42                                           def nested_flex():\n    43         1          2.0      2.0      0.1      root = YGNodeNew()\n    44        11          6.0      0.5      0.4      for i in range(10):\n    45        10         17.0      1.7      1.0          child = YGNodeNew()\n    46        10         11.0      1.1      0.7          YGNodeStyleSetFlex(child, 1)\n    47        10         14.0      1.4      0.8          YGNodeInsertChild(root, child, 0)\n    48\n    49       110         53.0      0.5      3.1          for ii in range(10):\n    50       100        197.0      2.0     11.7              grand_child = YGNodeNew()\n    51       100        111.0      1.1      6.6              YGNodeSetMeasureFunc(grand_child, measure_fn)\n    52       100        109.0      1.1      6.5              YGNodeStyleSetFlex(grand_child, 1)\n    53       100        121.0      1.2      7.2              YGNodeInsertChild(child, grand_child, 0)\n    54\n    55         1       1029.0   1029.0     61.1      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)\n    56         1         15.0     15.0      0.9      YGNodeFreeRecursive(root)\n\nTotal time: 0.093843 s\nFile: benchmark.py\nFunction: huge_nested_layout at line 59\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n    59                                           @profile\n    60                                           def huge_nested_layout():\n    61         1          2.0      2.0      0.0      root = YGNodeNew()\n    62        11          6.0      0.5      0.0      for i in range(10):\n    63        10         15.0      1.5      0.0          child = YGNodeNew()\n    64        10         11.0      1.1      0.0          YGNodeStyleSetFlexGrow(child, 1)\n    65        10         11.0      1.1      0.0          YGNodeStyleSetWidth(child, 10)\n    66        10         11.0      1.1      0.0          YGNodeStyleSetHeight(child, 10)\n    67        10         13.0      1.3      0.0          YGNodeInsertChild(root, child, 0)\n    68\n    69       110         44.0      0.4      0.0          for ii in range(10):\n    70       100        178.0      1.8      0.2              grand_child = YGNodeNew()\n    71       100        115.0      1.1      0.1              YGNodeStyleSetFlexDirection(grand_child, YGFlexDirection.Row)\n    72       100        101.0      1.0      0.1              YGNodeStyleSetFlexGrow(grand_child, 1)\n    73       100         97.0      1.0      0.1              YGNodeStyleSetWidth(grand_child, 10)\n    74       100         98.0      1.0      0.1              YGNodeStyleSetHeight(grand_child, 10)\n    75       100        114.0      1.1      0.1              YGNodeInsertChild(child, grand_child, 0)\n    76\n    77      1100        561.0      0.5      0.6              for iii in range(10):\n    78      1000       1782.0      1.8      1.9                  grand_grand_child = YGNodeNew()\n    79      1000       1037.0      1.0      1.1                  YGNodeStyleSetFlexGrow(grand_grand_child, 1)\n    80      1000        997.0      1.0      1.1                  YGNodeStyleSetWidth(grand_grand_child, 10)\n    81      1000        959.0      1.0      1.0                  YGNodeStyleSetHeight(grand_grand_child, 10)\n    82      1000       1177.0      1.2      1.3                  YGNodeInsertChild(grand_child, grand_grand_child, 0)\n    83\n    84     11000       5725.0      0.5      6.1                  for iiii in range(10):\n    85     10000      17682.0      1.8     18.8                      grand_grand_grand_child = YGNodeNew()\n    86     10000      11032.0      1.1     11.8                      YGNodeStyleSetFlexDirection(grand_grand_grand_child, YGFlexDirection.Row)\n    87     10000      10126.0      1.0     10.8                      YGNodeStyleSetFlexGrow(grand_grand_grand_child, 1)\n    88     10000      10035.0      1.0     10.7                      YGNodeStyleSetWidth(grand_grand_grand_child, 10)\n    89     10000       9814.0      1.0     10.5                      YGNodeStyleSetHeight(grand_grand_grand_child, 10)\n    90     10000      11796.0      1.2     12.6                      YGNodeInsertChild(grand_grand_child, grand_grand_grand_child, 0)\n    91\n    92         1       8696.0   8696.0      9.3      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)\n    93         1       1608.0   1608.0      1.7      YGNodeFreeRecursive(root)\n```\n",
    'author': 'dzhsurf',
    'author_email': 'dzhsurf@gmail.com',
    'maintainer': 'dzhsurf',
    'maintainer_email': 'dzhsurf@gmail.com',
    'url': 'https://github.com/dzhsurf/poga',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}
from src.build import *
build(setup_kwargs)

setup(**setup_kwargs)
