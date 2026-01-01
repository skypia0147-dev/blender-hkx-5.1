
import io_hkx_animation.prefs
import io_hkx_animation.props
import io_hkx_animation.ops

bl_info = {
    'name': "HKX Animation",
    'author': "Jonas Gernandt (Original), Smooth (Update)",
    'version': (1, 1, 0),
    'blender': (5, 1, 0),
    'location': "File > Import-Export",
    'description': "HKX Animation Import/Export for Skyrim, updated for Blender 5.1 Slotted Action API",
    'doc_url': "",
    'category': "Import-Export"}

def register():
    prefs.register()
    props.register()
    ops.register()

def unregister():
    ops.unregister()
    props.unregister()
    prefs.unregister()
