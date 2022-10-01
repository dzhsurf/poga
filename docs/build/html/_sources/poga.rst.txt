Poga Package
============


.. note:: Current Version

   Poga: 0.1.6

   YogaLayout: 1.19.0

How to install poga package?
----------------------------

.. code-block::

   pip install poga

   from poga import *

   def main():
      # use PogaLayout
      layout = PogaLayout(MyPogaView())
      # ...
      layout.apply_layout()

      # use capi directly
      node = YGNodeNew()
      YGNodeFree(node)


Submodules
----------

libpoga\_capi module
-------------------------

.. automodule:: poga.libpoga_capi
   :members:
   :show-inheritance:

poga\_layout module
------------------------

.. automodule:: poga.poga_layout
   :members:
   :show-inheritance:

poga\_view module
------------------------

.. automodule:: poga.poga_view
   :members:
   :show-inheritance:

