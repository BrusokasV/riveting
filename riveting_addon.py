bl_info = {
    "name": "Riveting",
    "author": "Vladislav Brusokas",
    "version": (0,0,1),
    "blender": (4, 2, 0),
    "location": "3D Viewport > Sidebar > Riveting category",
    "description": "In future, this addon will allow users to distribute rivets on meshes",
    "category": "Development",
}

import bpy

class VIEW3D_PT_riveting_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    bl_category = "Riveting"
    bl_label = "Riveting"
    
    def draw(self, context):
        row = self.layout.row()
        row.operator("mesh.primitive_cube_add", text="Placeholder Op")
        
def register():
    bpy.utils.register_class(VIEW3D_PT_riveting_panel)
    
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_riveting_panel)
    
    
if __name__ == "__main__":
    register()