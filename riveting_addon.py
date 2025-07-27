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
import bmesh

class MESH_OT_add_rivets(bpy.types.Operator):
    bl_idname = "mesh.add_rivets"
    bl_label = "Add Rivets to the Mesh"
    bl_options = {"REGISTER", "UNDO"}
    
    value: bpy.props.FloatProperty(
        name="Value",
        default=0.5,
        description="The editable value",
    )
    
    def execute(self, context):
        
        mesh_obj = bpy.context.active_object
        
        bm = bmesh.new()
        
        bm.from_mesh(mesh_obj.data)
        
        bmesh.ops.bevel(bm, geom=bm.verts, offset=self.value)
        
        bm.normal_update()
        
        bm.to_mesh(mesh_obj.data)
        
        mesh_obj.data.update()
        
        bm.free()
        
        #bpy.ops.mesh.primitive_monkey_add(size=self.mesh_size)
        
        return {"FINISHED"}

class VIEW3D_PT_riveting_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    bl_category = "Riveting"
    bl_label = "Riveting"
    
    def draw(self, context):
        row = self.layout.row()
        row.operator("mesh.add_rivets", text="Add Rivets")
        
def register():
    bpy.utils.register_class(VIEW3D_PT_riveting_panel)
    bpy.utils.register_class(MESH_OT_add_rivets)
    
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_riveting_panel)
    bpy.utils.unregister_class(MESH_OT_add_rivets)
    
    
if __name__ == "__main__":
    register()