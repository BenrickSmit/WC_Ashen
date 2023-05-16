bl_info = {
    "name" : "AshenShaders",
    "author" : "Benrick G. Smit",
    "version" : (1, 0),
    "blender" : (3, 50, 0),
    "location" : "View3D > AC Materials",
    "warning" : "These Textures will clear all textures already on the objects",
    "wiki_url" : "",
    "category" : "Texture/Shader Pack"
}

import bpy


"""GLOBAL SETTINGS - Bad Practice I Know"""
TOON_BSDF_NAME = 'Toon BSDF'
WATERCOLOR_BSDF_NAME = 'Watercolor BSDF'

NODE_SPACING = 300

# Rocks
SILVER_WC_ROCK_NAME = 'Silver WC Rock Material'
BROWN_WC_ROCK_NAME = 'Brown WC Rock Material'
BLUE_WC_ROCK_NAME = 'Blue WC Rock Material'
RED_WC_ROCK_NAME = 'Red WC Rock Material'
BLACK_WC_ROCK_NAME = 'Black WC Rock Material'
EMERALD_WC_ROCK_NAME = 'Emerald WC Rock Material'
SAPPHIRE_WC_ROCK_NAME = 'Sapphire WC Rock Material'
MAGIC_WC_ROCK_NAME = 'Magic WC Rock Material'
GRASSY_WC_ROCK_NAME = 'Grassy WC Rock Material'
JADE_WC_ROCK_NAME = 'Jade WC Rock Material'
TURTLE_WC_ROCK_NAME = 'Turtle WC Rock Material'

# Terrain
SUMMER_WC_GROUND_NAME = "Summer Ground WC Material"
AUTUMN_WC_GROUND_NAME = "Autumn Ground WC Material"
WINTER_WC_GROUND_NAME = "Winter Ground WC Material"
GRASS_DIRT_WC_GROUND_NAME = "Grass and Dirt Ground WC Material"
DIRT_WC_GROUND_NAME = "Dirt Ground WC Material"

# Trees
NORMAL_WC_TREE_NAME = "Normal Tree WC Material"

# Water
NORMAL_WC_WATER_NAME = "Normal Water WC Material"

# Crystals
SINGLE_WC_CRYSTAL_NAME = "Single Crystal WC Geometry"
GROUP_WC_CRYSTAL_NAME = "Group Crystal WC Geometry"
GROWING_WC_CRYSTAL_NAME = "Growing Crystal WC Geometry"
Spherical_WC_CRYSTAL_NAME = "Spherical Crystal WC Geometry"
CONAL_WC_CRYSTAL_NAME = "Conal Crystal WC Geometry"



point1x = 0.1681
point1y = 0.0187
point2x = 0.4681
point2y = 0.3625
point3x = 0.6909
point3y = 0.8375


#hex_colors = [0x637340, 0x475F4F, 0xEFE987 ,0xBCBF5E ,0xC2C667C] # Mossy Ground
#hex_colors = [0xFBC956, 0x9C8513,0x474D29, 0x8B9C4C, 0xBFA663] # Dessert Rocks Fields
#hex_colors = [0xFBC956, 0x9C8513, 0xBFA663, 0x8B9C4C, 0x474D29] # Dessert Fields
#hex_colors = [0x637340, 0x475F4F, 0xEFE987 ,0xBCBF5E ,0xC2C667C] # Mossy Ground
        
        

"""This Creates the Panel That will House the Shaders in the View3D Tab"""
class AshenShadersPanel_View3D(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport of Blender for Shaders"""
    bl_label = "Ashen Shaders"
    bl_idname = "SHADER_VIEW_MATERIALSPANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ashen Shader Library"
    
    def draw(self, context):
        layout = self.layout

        # Create a box to group the texture selection and operators
        box = layout.box()
        box.label(text="Texture Selection")
        box.prop(context.scene, "my_texture_property")

        # Create a column for the shader types
        col = layout.column()
        col.label(text="Rock Shaders")
        row = col.row(align=True)
        row.operator('shader.silver_rock_shader')
        row.operator('shader.brown_rock_shader')
        row = col.row(align=True)
        row.operator('shader.blue_rock_shader')
        row.operator('shader.red_rock_shader')
        row = col.row(align=True)
        row.operator('shader.black_rock_shader')
        row.operator('shader.emerald_rock_shader')
        row = col.row(align=True)
        row.operator('shader.sapphire_rock_shader')
        row.operator('shader.magic_rock_shader')
        row = col.row(align=True)
        row.operator('shader.grassy_rock_shader')
        row.operator('shader.jade_rock_shader')
        row = col.row(align=True)
        row.operator('shader.turtle_rock_shader')

        col.separator()

        col.label(text="Ground Shaders")
        row = col.row(align=True)
        row.operator('shader.summer_ground_shader')
        row.operator('shader.winter_ground_shader')
        row = col.row(align=True)
        row.operator('shader.autumn_ground_shader')
        row.operator('shader.grass_dirt_ground_shader')
        row = col.row(align=True)
        row.operator('shader.dirt_ground_shader')

        col.separator()

        col.label(text="Tree Shaders")
        col.operator('shader.normal_tree_shader')

        col.separator()

        col.label(text="Water Shaders")
        col.operator('shader.normal_water_shader')
        
        col.separator()
        col.label(text="Geometry Objects")
        col.operator('object.simple_geometry_node_operator')

        



"""This Creates the Panel that will House the Shaders in the Shaders Tab"""
class AshenShadersPanel_ShadersEditor(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport of Blender for Shaders"""
    bl_label = "Ashen Shaders"
    bl_idname = "SHADER_NODE_MATERIALSPANEL"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Ashen Shader Library"
    
    def draw(self, context):
        layout = self.layout

        # Create a box to group the texture selection and operators
        box = layout.box()
        box.label(text="Texture Selection")
        box.prop(context.scene, "my_texture_property")

        # Create a column for the shader types
        col = layout.column()
        col.label(text="Rock Shaders")
        row = col.row(align=True)
        row.operator('shader.silver_rock_shader')
        row.operator('shader.brown_rock_shader')
        row = col.row(align=True)
        row.operator('shader.blue_rock_shader')
        row.operator('shader.red_rock_shader')
        row = col.row(align=True)
        row.operator('shader.black_rock_shader')
        row.operator('shader.emerald_rock_shader')
        row = col.row(align=True)
        row.operator('shader.sapphire_rock_shader')
        row.operator('shader.magic_rock_shader')
        row = col.row(align=True)
        row.operator('shader.grassy_rock_shader')
        row.operator('shader.jade_rock_shader')
        row = col.row(align=True)
        row.operator('shader.turtle_rock_shader')

        col.separator()

        col.label(text="Ground Shaders")
        row = col.row(align=True)
        row.operator('shader.summer_ground_shader')
        row.operator('shader.winter_ground_shader')
        row = col.row(align=True)
        row.operator('shader.autumn_ground_shader')
        row.operator('shader.grass_dirt_ground_shader')
        row = col.row(align=True)
        row.operator('shader.dirt_ground_shader')

        col.separator()

        col.label(text="Tree Shaders")
        col.operator('shader.normal_tree_shader')

        col.separator()

        col.label(text="Water Shaders")
        col.operator('shader.normal_water_shader')


"""This creates some submenus that are easily operatable"""
class AsenShadersPanel_RockSubMenu(bpy.types.Operator):
    bl_idname = "object.rock_submenu"
    bl_label = "Rocks"
    bl_category = "AshenShaders/Submenu"

    def execute(self, context):
        print("Hello World")
        row = layout.row()
        row.label(text= "Select Texture to Use")
        return {'FINISHED'}




"""Create the new materials"""
class SHADER_OT_WATERCOLOUR_SILVER(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Silver Rock"
    bl_idname = 'shader.silver_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x535C6B, 0xA4A4AC, 0xDCDFD6 ,0xBFC3B5 ,0xF1F2ED]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=SILVER_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        

        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_BROWN(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Brown Rock"
    bl_idname = 'shader.brown_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1681
        point1y = 0.0187
        point2x = 0.4681
        point2y = 0.3625
        point3x = 0.6909
        point3y = 0.8375

        # Colours
        
        #hex_colors = ['989189', 'AA9C8F', 'B8B5B0' ,'A29988' ,'8A8778']
        hex_colors = [0x989189, 0xAA9C8F, 0xB8B5B0 ,0xA29988 ,0x8A8778]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=BROWN_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}



class SHADER_OT_WATERCOLOUR_BLUE(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Blue Rock"
    bl_idname = 'shader.blue_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.3000
        point1y = 0.1125
        point2x = 0.5090
        point2y = 0.3500
        point3x = 0.6454
        point3y = 0.6375

        # Colours        
        hex_colors = [0x4B5171, 0xA5A8B9, 0x5E5F73 ,0x716E79 ,0x3D4262]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=BLUE_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_BLACK(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Black Rock"
    bl_idname = 'shader.black_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1545
        point1y = 0.1312
        point2x = 0.3545
        point2y = 0.4812
        point3x = 0.6545
        point3y = 0.6750

        # Colours        
        hex_colors = [0x293D3B, 0x202F28, 0x3B483F ,0x869582 ,0x5F6758]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=BLACK_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}




class SHADER_OT_WATERCOLOUR_RED(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Red Rock"
    bl_idname = 'shader.red_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.2181
        point1y = 0.1875
        point2x = 0.5590
        point2y = 0.3312
        point3x = 0.7363
        point3y = 0.7312

        # Colours        
        hex_colors = [0x927E80, 0x291D27, 0x6B5255 ,0xB3B0A9 ,0x07050A]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=RED_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}



class SHADER_OT_WATERCOLOUR_EMERALD(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Emerald Rock"
    bl_idname = 'shader.emerald_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1727
        point1y = 0.0812
        point2x = 0.3363
        point2y = 0.4687
        point3x = 0.6863
        point3y = 0.5187

        # Colours        
        hex_colors = [0x5A8E60, 0x104807, 0x89B34F ,0xC9F3B3 ,0x587B07]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=EMERALD_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}



class SHADER_OT_WATERCOLOUR_SAPPHIRE(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Sapphire Rock"
    bl_idname = 'shader.sapphire_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1909
        point1y = 0.0625
        point2x = 0.3636
        point2y = 0.4250
        point3x = 0.6818
        point3y = 0.6187

        # Colours        
        hex_colors = [0x3C86C7, 0x021F59, 0x5CA0EB ,0x053D9E ,0x73B7DC]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=SAPPHIRE_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}



class SHADER_OT_WATERCOLOUR_MAGIC(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Magic Rock"
    bl_idname = 'shader.magic_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.2318
        point1y = 0.0812
        point2x = 0.4590
        point2y = 0.2562
        point3x = 0.55
        point3y = 0.7375

        # Colours        
        hex_colors = [0x9B5031, 0xC5ACAF, 0x8778A1 ,0xD9CFD0 ,0xBE677A]

        
        # Create a new material
        new_material = bpy.data.materials.new(name=MAGIC_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_GRASSY(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Grassy Rock"
    bl_idname = 'shader.grassy_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.2
        point1y = 0.2375
        point2x = 0.2863
        point2y = 0.4812
        point3x = 0.6
        point3y = 0.6187

        # Colours        
        hex_colors = [0x395E3E, 0x7B8675, 0x4C753B ,0x364339 , 0xCFD9C1] #0x5C805A]#, 0xCFD9C1]
        
        
        # Create a new material
        new_material = bpy.data.materials.new(name=GRASSY_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_JADE(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Jade Rock"
    bl_idname = 'shader.jade_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1909
        point1y = 0.1312
        point2x = 0.3636
        point2y = 0.3625
        point3x = 0.7454
        point3y = 0.7375

        # Colours        
        hex_colors = [0x2C4D42, 0x389F84, 0x182D28 ,0x227F64 ,0x7CB799]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=JADE_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_TURTLE(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Turtle Rock"
    bl_idname = 'shader.turtle_rock_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.2227
        point1y = 0.15
        point2x = 0.3818
        point2y = 0.5
        point3x = 0.75
        point3y = 0.7250

        # Colours        
        hex_colors = [0x395F72, 0x9EC5CC, 0x00222B ,0x5C8484 ,0x7DAFB8]
        
        # Create a new material
        new_material = bpy.data.materials.new(name=TURTLE_WC_ROCK_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}








''' Create the Ground Textures '''
class SHADER_OT_WATERCOLOUR_SUMMER(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Summer Ground"
    bl_idname = 'shader.summer_ground_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x475F4F, 0x637340, 0xBCBF5E, 0xEFE987 ,0xC2C667C] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=SUMMER_WC_GROUND_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 24.5
        watercolor_group_node.inputs['Randomness'].default_value = 0.6
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_AUTUMN(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Autumn Ground"
    bl_idname = 'shader.autumn_ground_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0xFBC956, 0xBFA663, 0x9C8513, 0x8B9C4C, 0xDA9945] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=AUTUMN_WC_GROUND_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 24.5
        watercolor_group_node.inputs['Randomness'].default_value = 0.6
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_WINTER(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Winter Ground"
    bl_idname = 'shader.winter_ground_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x5D6C8C, 0xDFD8C6, 0x9098A5, 0xF2E6D8, 0x3D4B6E] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=WINTER_WC_GROUND_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 24.5
        watercolor_group_node.inputs['Randomness'].default_value = 0.6
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_DIRT(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Dirt Ground"
    bl_idname = 'shader.dirt_ground_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x1C0F09, 0xAE7F23, 0x695F2C, 0x7F5C24, 0x5F2B16] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=DIRT_WC_GROUND_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 24.5
        watercolor_group_node.inputs['Randomness'].default_value = 0.6
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}


class SHADER_OT_WATERCOLOUR_GRASS_DIRT(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Grass and Dirt Ground"
    bl_idname = 'shader.grass_dirt_ground_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x1A2713, 0x6F9B20, 0xDECF38, 0x8F6B31, 0x2B3711 ] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=GRASS_DIRT_WC_GROUND_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 24.5
        watercolor_group_node.inputs['Randomness'].default_value = 0.6
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}





''' TREE SHADERS '''
class SHADER_OT_WATERCOLOUR_NORMAL_TREE(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Normal Tree"
    bl_idname = 'shader.normal_tree_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x472F0D, 0x8D7946, 0x46321A, 0x5E6544, 0x301D0F ] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=NORMAL_WC_TREE_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 9.2
        watercolor_group_node.inputs['Randomness'].default_value = 1
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}







''' WATER SHADERS'''
class SHADER_OT_WATERCOLOUR_NORMAL_WATER(bpy.types.Operator):
    """Creates a Shader That can be used"""
    bl_label = "Normal Water"
    bl_idname = 'shader.normal_water_shader'
    
    def execute(self, context):
        # Setup the Colour Properties
        # Color Curve
        point1x = 0.1818
        point1y = 0.0687
        point2x = 0.3727
        point2y = 0.3062
        point3x = 0.7090
        point3y = 0.8625

        # Colours        
        hex_colors = [0x405673, 0x91BDD9, 0xE8FFFF, 0x95DBE3, 0xF2F2F2 ] # Summer Fields
        
        # Create a new material
        new_material = bpy.data.materials.new(name=NORMAL_WC_WATER_NAME)
        new_material.use_nodes = True
        new_material.node_tree.nodes.clear()

        # Move to Node_Editor
        bpy.context.area.type = 'NODE_EDITOR'

        # Add the group node to the new material
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        
        watercolor_group_name = WATERCOLOR_BSDF_NAME
        watercolor_group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == watercolor_group_name:
                watercolor_group_node = node
                break

        # If the group node doesn't exist, create it
        if watercolor_group_node is None:
            watercolor_group_node = new_material.node_tree.nodes.new(type='ShaderNodeGroup')
            watercolor_group_node.node_tree = create_waterpaint_shader(context, self, watercolor_group_name)

        # Set some properties dynamically to ensure different materials
        # Find the "FinalColours" node in the group node
        final_colors_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "FinalColours":
                final_colors_node = node
                break

        # Set the color ramp of the "FinalColours" node to specific colors
        colors = [hex_to_rgb(hex_color) for hex_color in hex_colors] # Replace with your specific colors
        color_ramp = final_colors_node.color_ramp
        for i, color in enumerate(colors):
            pos = i / (len(colors) - 1)
            color_ramp.elements[i].position = pos
            color_ramp.elements[i].color = color
        
        
        # Find the "RGBColorCurves" node in the group node
        final_colors_curves_node = None
        for node in watercolor_group_node.node_tree.nodes:
            if node.name == "RGBColorCurves":
                final_colors_curves_node = node
                break
            
        curve_c = final_colors_curves_node.mapping.curves[3]

        # Add the new points to the curve
        curve_c.points.new(point1x, point1y)
        curve_c.points.new(point2x, point2y)
        curve_c.points.new(point3x, point3y)

        # Update curve. Now new points are [0],[1],[2] and last one is [3]
        final_colors_curves_node.mapping.update()
        
        
        # Create the necessary Material
        material_output_node = new_material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
        material_output_node.location = (200, 0)
        
        object_info_node = new_material.node_tree.nodes.new(type="ShaderNodeObjectInfo")
        object_info_node.location = (-300, -250)
        
        texture_coord_node = new_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
        texture_coord_node.location = (-300, 0)
        
        
        # Connect it to the material output as well
        new_material.node_tree.links.new(watercolor_group_node.outputs['BSDF'], material_output_node.inputs['Surface'])
        new_material.node_tree.links.new(object_info_node.outputs['Location'], watercolor_group_node.inputs['Obj Location'])
        new_material.node_tree.links.new(texture_coord_node.outputs['Generated'], watercolor_group_node.inputs['Obj Generated'])
        
        # Set the final settings of the material
        watercolor_group_node.inputs['Texture Scale'].default_value = 32
        watercolor_group_node.inputs['Randomness'].default_value = 0.6
        watercolor_group_node.inputs['Rock Highlight Scale'].default_value = 0.8
        
        
        # Set the material as active
        bpy.context.object.active_material = new_material

        # Move to 3D Viewer
        bpy.context.area.type = 'VIEW_3D'
        
        return {'FINISHED'}

















''' Geometry Nodes For Advanced Options'''
class SimpleGeometryNodeOperator(bpy.types.Operator):
    """Create a simple geometry node tree and modify it"""
    bl_idname = "object.simple_geometry_node_operator"
    bl_label = "Simple Crystal"
    
    def execute(self, context):
        '''# Create a new cube object
        bpy.ops.mesh.primitive_cube_add()
        base_cube = bpy.context.object

        # Select the cube object
        bpy.context.view_layer.objects.active = base_cube
        base_cube.select_set(True)

        # Add the Geometry Nodes modifier
        crystal_modifier = base_cube.modifiers.new("Crystal Geometry", type='NODES')

        # Add the basic connections
        bpy.ops.node.new_geometry_node_group_assign()
        
        # Clear the crystal_modifier from all nodes
        crystal_modifier.node_group.nodes.clear()


        # Add a Mesh node
        input_node = crystal_modifier.node_group.nodes.new('NodeGroupInput')
        output_node = crystal_modifier.node_group.nodes.new('NodeGroupOutput')
        #input_socket = input_node.outputs.new('NodeSocketGeometry', 'Geometry')
        #output_socket = output_node.inputs.new('NodeSocketGeometry', 'Geometry')
        input_node.name = "MyInputNode"
        output_node.name = "MyOutputNode"
        input_node.location = (-1400, 0)
        output_node.location = (2200, 0)

        
        base_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeMeshCylinder')
        base_mesh_node.name = "MyBaseCylinderMesh"
        base_mesh_node.location = (-600, 0)

        extrude_base_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeExtrudeMesh')
        extrude_base_mesh_node.name = "ExtrudeBaseMesh"

        scale_base_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeScaleElements')
        scale_base_mesh_node.name = "ScaleBaseModifier"
        scale_base_mesh_node.location = (200, 0)

        boolean_base_mesh_node = crystal_modifier.node_group.nodes.new('FunctionNodeBooleanMath')
        boolean_base_mesh_node.name = "BooleanBaseMeth"
        boolean_base_mesh_node.location = (-300, -200)

        merge_by_distance_new_mesh = crystal_modifier.node_group.nodes.new('GeometryNodeMergeByDistance')
        merge_by_distance_new_mesh.name = "MergeMeshForNewMesh"
        merge_by_distance_new_mesh.location = (400, 0)

        first_dual_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeDualMesh')
        first_dual_mesh_node.name = "FirstDualMeshNode"
        first_dual_mesh_node.location = (600, 0)
        
        second_dual_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeDualMesh')
        second_dual_mesh_node.name = "SecondDualMeshNode"
        second_dual_mesh_node.location = (1000, 0)

        triangulate_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeTriangulate')
        triangulate_mesh_node.name = "MeshTriangulation"
        triangulate_mesh_node.location = (800, 0)

        subdivide_mesh_node = crystal_modifier.node_group.nodes.new('GeometryNodeSubdivideMesh')
        subdivide_mesh_node.name = 'SubdivideFinalMesh'
        subdivide_mesh_node.location = (1200, 0)

        shade_smooth_final_node = crystal_modifier.node_group.nodes.new('GeometryNodeSetShadeSmooth')
        shade_smooth_final_node.name = 'FinalSmoothShade'
        shade_smooth_final_node.location = (2000, 0)


        set_material_node = crystal_modifier.node_group.nodes.new('GeometryNodeSetMaterial')
        set_material_node.name = 'SetCrystalMaterialNode'
        set_material_node.location = (1800, 0)


        set_position_node = crystal_modifier.node_group.nodes.new('GeometryNodeSetPosition')
        set_position_node.name = 'DisplacementPositionNode'
        set_position_node.location = (1600, 0)


        crystal_geometry_texture_math_node = crystal_modifier.node_group.nodes.new('ShaderNodeVectorMath')
        crystal_geometry_texture_math_node.name = 'GeometryTextureScale'
        crystal_geometry_texture_math_node.location = (1400, -200)

        crystal_geometry_texture_range_node = crystal_modifier.node_group.nodes.new('ShaderNodeMapRange')
        crystal_geometry_texture_range_node.name = 'GeometryTextureMapRange'
        crystal_geometry_texture_range_node.location = (1200, -200)


        crystal_geometry_texture_displacement_node = crystal_modifier.node_group.nodes.new('ShaderNodeTexMusgrave')
        crystal_geometry_texture_displacement_node.name = 'GeometryTextureDisplacement'
        crystal_geometry_texture_displacement_node.location = (1000, -200)

        # Set some default settings of the nodes
        base_mesh_node.inputs[0].default_value = 6
        boolean_base_mesh_node.operation = 'NOT'
        scale_base_mesh_node.inputs['Scale'].default_value = 0
        crystal_geometry_texture_math_node.operation = 'SCALE'
        crystal_geometry_texture_range_node.data_type = 'FLOAT_VECTOR' 
        crystal_geometry_texture_range_node.interpolation_type = 'LINEAR' #LINEAR #STEPPED #SMOOTHERSTEP #SMOOTHSTEP
        crystal_geometry_texture_displacement_node.musgrave_type = 'RIDGED_MULTIFRACTAL'
        crystal_geometry_texture_displacement_node.musgrave_dimensions = '4D'

        # Connect the output node to the base mesh node
        #           crystal_modifier.node_group.links.new()
        crystal_modifier.node_group.links.new(base_mesh_node.outputs['Mesh'], extrude_base_mesh_node.inputs['Mesh'])
        crystal_modifier.node_group.links.new(extrude_base_mesh_node.outputs['Mesh'], scale_base_mesh_node.inputs['Geometry'])
        crystal_modifier.node_group.links.new(extrude_base_mesh_node.outputs['Mesh'], scale_base_mesh_node.inputs['Geometry'])
        crystal_modifier.node_group.links.new(base_mesh_node.outputs['Side'], boolean_base_mesh_node.inputs['Boolean'])
        crystal_modifier.node_group.links.new(boolean_base_mesh_node.outputs['Boolean'], extrude_base_mesh_node.inputs['Selection'])
        crystal_modifier.node_group.links.new(extrude_base_mesh_node.outputs['Top'], scale_base_mesh_node.inputs['Selection'])
        crystal_modifier.node_group.links.new(second_dual_mesh_node.outputs['Dual Mesh'], subdivide_mesh_node.inputs['Mesh'])
        crystal_modifier.node_group.links.new(scale_base_mesh_node.outputs['Geometry'], merge_by_distance_new_mesh.inputs['Geometry'])
        crystal_modifier.node_group.links.new(merge_by_distance_new_mesh.outputs['Geometry'], first_dual_mesh_node.inputs['Mesh'] )
        crystal_modifier.node_group.links.new(first_dual_mesh_node.outputs['Dual Mesh'], triangulate_mesh_node.inputs['Mesh'] )
        crystal_modifier.node_group.links.new(second_dual_mesh_node.outputs['Dual Mesh'], output_node.inputs['Geometry'] )
        crystal_modifier.node_group.links.new(triangulate_mesh_node.outputs['Mesh'], second_dual_mesh_node.inputs['Mesh'])
        crystal_modifier.node_group.links.new(subdivide_mesh_node.outputs['Mesh'], set_position_node.inputs['Geometry'])
        crystal_modifier.node_group.links.new(set_position_node.outputs['Geometry'] , set_material_node.inputs['Geometry'])
        crystal_modifier.node_group.links.new(set_material_node.outputs['Geometry']  , shade_smooth_final_node.inputs['Geometry'])
        crystal_modifier.node_group.links.new(shade_smooth_final_node.outputs['Geometry'], output_node.inputs['Geometry'])

        crystal_modifier.node_group.links.new(crystal_geometry_texture_math_node.outputs['Vector'], set_position_node.inputs['Offset'])
        crystal_modifier.node_group.links.new(crystal_geometry_texture_range_node.outputs['Vector'], crystal_geometry_texture_math_node.inputs['Vector'])
        crystal_modifier.node_group.links.new(crystal_geometry_texture_displacement_node.outputs[0], crystal_geometry_texture_range_node.inputs['Vector'])
        '''


        # Create a new cube object
        bpy.ops.mesh.primitive_cube_add()
        base_cube = bpy.context.object

        # Select the cube object
        bpy.context.view_layer.objects.active = base_cube
        base_cube.select_set(True)

        # Add the Geometry Nodes modifier
        crystal_modifier = base_cube.modifiers.new("Crystal Geometry", type='NODES')

        # Add the basic connections
        bpy.ops.node.new_geometry_node_group_assign()

        # Clear the crystal_modifier from all nodes
        crystal_modifier.node_group.nodes.clear()

        # Create the custom geometry node group
        node_group = create_ridgid_crystal_geometry_node_group()

        # Set the node group for the modifier
        crystal_modifier.node_group = node_group

        return {'FINISHED'}



















































class SHADER_OT_SIMPLE_TOON_BSDF(bpy.types.Operator):
    bl_label = "Simple Toon Shader"
    bl_idname = "shader.toon_simple_shader"
    
    def execute (self, context):
        # Check if the current node tree has the group node already
        current_tree = context.space_data.edit_tree
        group_name = TOON_BSDF_NAME
        group_node = None
        for node in current_tree.nodes:
            if node.type == 'GROUP' and node.node_tree.name == group_name:
                group_node = node
                break

        # If the group node doesn't exist, create it
        if not group_node:
            group_node = current_tree.nodes.new(type='ShaderNodeGroup')
            group_node.node_tree = create_toon_shader(context, self, group_name)

        # Select the group node and set it as the active node
        current_tree.nodes.active = group_node
        group_node.select = True
        
        return {"FINISHED"}






""" FUNCTION TO CREATE THE WATERPAINT SHADER THAT IS THE BASIS OF THE PACK"""
def create_waterpaint_shader(Context, operator, group_name):
    """Creates a Waterapoint Shader that can be used"""
    
    # Enable the use of Nodes      
    bpy.context.scene.use_nodes = True

    # Create a new node group
    watercolor_bsdf_group = bpy.data.node_groups.new(name=WATERCOLOR_BSDF_NAME, type="ShaderNodeTree")


    # Create the Group nodes and input and output nodes
    group_input_node = watercolor_bsdf_group.nodes.new(type='NodeGroupInput')
    group_input_node.name = "InputNode"
    group_output_node = watercolor_bsdf_group.nodes.new(type="NodeGroupOutput")
    group_output_node.name = "OutputNode"
    toon_bsdf_group = create_toon_shader(watercolor_bsdf_group, Context, TOON_BSDF_NAME)
    group_node = watercolor_bsdf_group.nodes.new(type='ShaderNodeGroup')
    group_node.node_tree = toon_bsdf_group
        
    
    # Create the rest of the nodes
    rgb_curves_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeRGBCurve")
    rgb_curves_node.name = "RGBColorCurves"
    randomness_noise_texture_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexNoise")
    randomness_noise_texture_node.name = "Randomness Noise Texture "
    mix_color_randomness_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMixRGB")
    mix_color_randomness_node.name = "Mix Color Randomness"
    randomness_mapping_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMapping")
    randomness_mapping_node.name = "Mapping Randomness"
    voronoi_texture_big_detail_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexVoronoi")
    voronoi_texture_big_detail_node.name = "Voronoi Texture Big Detail"
    multiply_watercolor_patterns_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeVectorMath")
    multiply_watercolor_patterns_node.operation = "MULTIPLY"
    multiply_watercolor_patterns_node.name = "Multiply Watercolor Patterns"
    voronoi_texture_small_detail_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexVoronoi")
    voronoi_texture_small_detail_node.name = "Voronoi Texture Small Detail"    
    softlight_mix_color_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMixRGB")
    softlight_mix_color_node.name = "Mix Watercolor Brushes"
    shadow_mix_color_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMixRGB")
    shadow_mix_color_node.name = "Mix Highlights and Shadows"
    watercolor_texture_size_multiply = watercolor_bsdf_group.nodes.new(type="ShaderNodeMath")
    watercolor_texture_size_multiply.operation = "MULTIPLY"
    watercolor_texture_size_multiply.name = "Vector Multiply"
    highlights_mix_colour_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMixRGB")
    highlights_mix_colour_node.name = "Mix Highlight Colour with Watercolour"
    map_wc_uneven_brush_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMapRange")
    map_wc_uneven_brush_node.name = "Map Watercolor Uneven Brush to Smoothness"
    map_wc_mixing_brush_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMapRange")
    map_wc_mixing_brush_node.name = "Map Watercolor Mixing to Randomness"
    color_ramp_uneven_brush_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeValToRGB")
    color_ramp_uneven_brush_node.name = "Color Ramp Uneven Brush"  
    color_ramp_mixing_brush_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeValToRGB")
    color_ramp_mixing_brush_node.name = "Color Ramp Mixing Brush"
    noise_texture_uneven_brush_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexNoise")
    noise_texture_uneven_brush_node.name = "Noise Texture for Uneven Brushing"
    noise_texture_mixing_brush_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexNoise")
    noise_texture_mixing_brush_node.name = "Noise Texture for Mixing Brushing"
    color_ramp_highlights_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeValToRGB")
    color_ramp_highlights_node.name = "Color Ramp for Artificial Highlights"
    color_ramp_shadows_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeValToRGB")
    color_ramp_shadows_node.name = "Color Ramp for Artificial Shadows"
    gradient_highlights_texture_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexGradient")
    gradient_highlights_texture_node.name = "Gradient Texture for Highlights"
    gradient_shadows_texture_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeTexGradient")
    gradient_shadows_texture_node.name = "Gradient Texture for Shadows"
    map_vector_gradient_shadows_node = watercolor_bsdf_group.nodes.new(type="ShaderNodeMapping")
    map_vector_gradient_shadows_node.name = "Map Vector for Shadows"
    map_vector_gradient_highlights_node = watercolor_bsdf_group.nodes.new(type='ShaderNodeMapping')
    map_vector_gradient_highlights_node.name = "Map Vector for Highlights"
    color_ramp_finalColours = watercolor_bsdf_group.nodes.new(type="ShaderNodeValToRGB")
    color_ramp_finalColours.name = "FinalColours"
    math_subtract_node_shadows = watercolor_bsdf_group.nodes.new(type="ShaderNodeMath")
    math_multiply_node_highlights = watercolor_bsdf_group.nodes.new(type="ShaderNodeMath")

    # Create the Inputs and Outputs of the group
    # Colour Selection
    """watercolor_bsdf_group.inputs.new('NodeSocketColor', 'Color1')
    watercolor_bsdf_group.inputs['Color1'].default_value = (1, 1, 1, 1)
    watercolor_bsdf_group.inputs.new('NodeSocketColor', 'Color2')
    watercolor_bsdf_group.inputs['Color2'].default_value = (1, 1, 1, 1)
    watercolor_bsdf_group.inputs.new('NodeSocketColor', 'Color3')
    watercolor_bsdf_group.inputs['Color3'].default_value = (1, 1, 1, 1)
    watercolor_bsdf_group.inputs.new('NodeSocketColor', 'Color4')
    watercolor_bsdf_group.inputs['Color4'].default_value = (1, 1, 1, 1)
    watercolor_bsdf_group.inputs.new('NodeSocketColor', 'Color5')
    watercolor_bsdf_group.inputs['Color5'].default_value = (1, 1, 1, 1)
    """
    
    # Set the final colour ramp colours
    color_ramp_finalColours.color_ramp.elements.new(0.2)
    color_ramp_finalColours.color_ramp.elements.new(0.5)
    color_ramp_finalColours.color_ramp.elements.new(0.8)
    
    # Variability
    watercolor_bsdf_group.inputs.new('NodeSocketVector', 'Obj Generated')
    watercolor_bsdf_group.inputs['Obj Generated'].default_value = (1, 1, 1)
    watercolor_bsdf_group.inputs.new('NodeSocketVector', 'Obj Location')
    watercolor_bsdf_group.inputs['Obj Location'].default_value = (1, 1, 1)
    
    # Normal Scalars
    watercolor_bsdf_group.inputs.new('NodeSocketFloat', 'Texture Scale')
    watercolor_bsdf_group.inputs['Texture Scale'].default_value = 9.3
    watercolor_bsdf_group.inputs.new('NodeSocketFloat', 'Randomness')
    watercolor_bsdf_group.inputs['Randomness'].default_value = 0.4
    watercolor_bsdf_group.inputs.new('NodeSocketFloat', 'Blend Scale')
    watercolor_bsdf_group.inputs['Blend Scale'].default_value = 1
    watercolor_bsdf_group.inputs.new('NodeSocketFloat', 'Rock Highlight Scale')
    watercolor_bsdf_group.inputs['Rock Highlight Scale'].default_value = 1
    watercolor_bsdf_group.inputs.new('NodeSocketFloat', 'WC Mixing Scale')
    watercolor_bsdf_group.inputs['WC Mixing Scale'].default_value = 2
    
    
    watercolor_bsdf_group.outputs.new('NodeSocketShader', 'BSDF')

    # Arrange in a grid for ... reasons
    
    num_rows = 5
    num_cols = 8
        
    for index, node in enumerate(watercolor_bsdf_group.nodes):
        # Calculate the position of the node based on its index
        row_index = index // num_cols
        col_index = index % num_cols
        x = NODE_SPACING * (col_index - 0.5 * (num_cols - 1))
        y = NODE_SPACING * (row_index - 0.5 * (num_rows - 1))

        # Set the location of the node
        node.location = (x, y) 
      
      
    
    # Create the Connections
    watercolor_bsdf_group.links.new(color_ramp_finalColours.outputs['Color'], rgb_curves_node.inputs['Color'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Randomness'], randomness_noise_texture_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], randomness_noise_texture_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(randomness_noise_texture_node.outputs['Fac'], mix_color_randomness_node.inputs['Color1'])
    watercolor_bsdf_group.links.new(mix_color_randomness_node.outputs['Color'], randomness_mapping_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], randomness_mapping_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Location'], randomness_mapping_node.inputs['Location'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], randomness_mapping_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(randomness_mapping_node.outputs['Vector'], voronoi_texture_big_detail_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(voronoi_texture_big_detail_node.outputs['Color'], softlight_mix_color_node.inputs['Color1'])
    watercolor_bsdf_group.links.new(voronoi_texture_small_detail_node.outputs['Color'], softlight_mix_color_node.inputs['Color2'])
    watercolor_bsdf_group.links.new(softlight_mix_color_node.outputs['Color'], shadow_mix_color_node.inputs['Color2'])
    watercolor_bsdf_group.links.new(randomness_mapping_node.outputs['Vector'], multiply_watercolor_patterns_node.inputs[0])
    watercolor_bsdf_group.links.new(multiply_watercolor_patterns_node.outputs['Vector'], voronoi_texture_small_detail_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Texture Scale'], watercolor_texture_size_multiply.inputs[0])
    watercolor_bsdf_group.links.new(watercolor_texture_size_multiply.outputs[0], voronoi_texture_small_detail_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Texture Scale'], voronoi_texture_big_detail_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(shadow_mix_color_node.outputs['Color'], highlights_mix_colour_node.inputs['Color1'])
    watercolor_bsdf_group.links.new(highlights_mix_colour_node.outputs['Color'], color_ramp_finalColours.inputs['Fac'])
    watercolor_bsdf_group.links.new(map_wc_uneven_brush_node.outputs['Result'], voronoi_texture_big_detail_node.inputs['Smoothness'])
    watercolor_bsdf_group.links.new(map_wc_uneven_brush_node.outputs['Result'], voronoi_texture_small_detail_node.inputs['Smoothness'])
    watercolor_bsdf_group.links.new(map_wc_mixing_brush_node.outputs['Result'], voronoi_texture_big_detail_node.inputs['Randomness'])
    watercolor_bsdf_group.links.new(map_wc_mixing_brush_node.outputs['Result'], voronoi_texture_small_detail_node.inputs['Randomness'])
    watercolor_bsdf_group.links.new(noise_texture_uneven_brush_node.outputs['Fac'], color_ramp_uneven_brush_node.inputs['Fac'])
    watercolor_bsdf_group.links.new(noise_texture_mixing_brush_node.outputs['Fac'], color_ramp_mixing_brush_node.inputs['Fac']) 
    watercolor_bsdf_group.links.new(randomness_mapping_node.inputs['Vector'], noise_texture_uneven_brush_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(randomness_mapping_node.inputs['Vector'], noise_texture_mixing_brush_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], noise_texture_uneven_brush_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], noise_texture_mixing_brush_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Blend Scale'], noise_texture_uneven_brush_node.inputs['Detail'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Blend Scale'], noise_texture_mixing_brush_node.inputs['Detail'])
    watercolor_bsdf_group.links.new(color_ramp_uneven_brush_node.outputs['Color'], map_wc_uneven_brush_node.inputs['Value'])
    watercolor_bsdf_group.links.new(color_ramp_mixing_brush_node.outputs['Color'], map_wc_mixing_brush_node.inputs['Value'])
    if group_node.inputs['Color']:
        watercolor_bsdf_group.links.new(rgb_curves_node.outputs['Color'], group_node.inputs['Color'])
    if group_node.outputs['Surface']:
        watercolor_bsdf_group.links.new(group_node.outputs['Surface'], group_output_node.inputs['BSDF'])
    
    watercolor_bsdf_group.links.new(color_ramp_shadows_node.outputs['Color'], shadow_mix_color_node.inputs['Color1'])
    watercolor_bsdf_group.links.new(color_ramp_highlights_node.outputs['Color'], highlights_mix_colour_node.inputs['Fac'])
    watercolor_bsdf_group.links.new(gradient_shadows_texture_node.outputs['Color'], color_ramp_shadows_node.inputs['Fac'])
    watercolor_bsdf_group.links.new(gradient_highlights_texture_node.outputs['Color'], color_ramp_highlights_node.inputs['Fac'])
    
    watercolor_bsdf_group.links.new(group_input_node.outputs['Rock Highlight Scale'], math_subtract_node_shadows.inputs[0])
    watercolor_bsdf_group.links.new(math_subtract_node_shadows.outputs['Value'], map_vector_gradient_shadows_node.inputs['Scale'])
    
    watercolor_bsdf_group.links.new(math_multiply_node_highlights.outputs['Value'], map_vector_gradient_highlights_node.inputs['Scale'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Rock Highlight Scale'], math_multiply_node_highlights.inputs[0])
    
    
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], map_vector_gradient_shadows_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], map_vector_gradient_highlights_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Location'], map_vector_gradient_shadows_node.inputs['Location'])
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Location'], map_vector_gradient_highlights_node.inputs['Location'])
    watercolor_bsdf_group.links.new(map_vector_gradient_shadows_node.outputs['Vector'], gradient_shadows_texture_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(map_vector_gradient_highlights_node.outputs['Vector'], gradient_highlights_texture_node.inputs['Vector'])
    
    
    watercolor_bsdf_group.links.new(randomness_mapping_node.outputs['Vector'], noise_texture_uneven_brush_node.inputs['Vector'])
    watercolor_bsdf_group.links.new(randomness_mapping_node.outputs['Vector'], noise_texture_mixing_brush_node.inputs['Vector'])
    
    watercolor_bsdf_group.links.new(group_input_node.outputs['Obj Generated'], randomness_mapping_node.inputs['Vector'])
    
    #watercolor_bsdf_group.links.new()
    
    # Setup the Default Values
    randomness_noise_texture_node.inputs['Detail'].default_value = 11.800
    randomness_noise_texture_node.inputs['Roughness'].default_value = 0.567
    randomness_noise_texture_node.inputs['Distortion'].default_value = 5.4
    mix_color_randomness_node.inputs['Color2'].default_value = (0, 0, 0, 0)
    mix_color_randomness_node.inputs['Fac'].default_value = 0.25
    randomness_mapping_node
    voronoi_texture_big_detail_node.feature = "SMOOTH_F1"
    voronoi_texture_big_detail_node.distance = 'CHEBYCHEV'
    voronoi_texture_small_detail_node.feature = "SMOOTH_F1"
    voronoi_texture_small_detail_node.distance = 'CHEBYCHEV'
    softlight_mix_color_node.inputs['Fac'].default_value = 0.783
    softlight_mix_color_node.blend_type = "SOFT_LIGHT"
    shadow_mix_color_node.blend_type = "MULTIPLY"
    shadow_mix_color_node.inputs['Fac'].default_value = 0.808
    multiply_watercolor_patterns_node.inputs[1].default_value = (1.2, 1.2, 1.2)
    watercolor_texture_size_multiply.inputs[1].default_value = 2.8
    highlights_mix_colour_node.inputs['Color2'].default_value = (1, 1, 1, 1)
    map_wc_uneven_brush_node.inputs['From Min'].default_value = 0.1
    map_wc_mixing_brush_node.inputs['From Min'].default_value = 0.1
    map_wc_uneven_brush_node.inputs['From Max'].default_value = 1.0
    map_wc_mixing_brush_node.inputs['From Max'].default_value = 1.0
    map_wc_uneven_brush_node.inputs['To Min'].default_value = 0.3
    map_wc_mixing_brush_node.inputs['To Min'].default_value = 0.3
    map_wc_uneven_brush_node.inputs['To Max'].default_value = 0.9
    map_wc_mixing_brush_node.inputs['To Max'].default_value = 0.9
    #color_ramp_uneven_brush_node.elements.new(0.2)
    color_ramp_uneven_brush_node.color_ramp.elements[0].position = 0.477
    color_ramp_uneven_brush_node.color_ramp.elements[1].position = 0.545
    #color_ramp_mixing_brush_node.elements.new(0.2)
    color_ramp_mixing_brush_node.color_ramp.elements[0].position = 0.450
    color_ramp_mixing_brush_node.color_ramp.elements[1].position = 0.668
    noise_texture_uneven_brush_node.inputs['Roughness'].default_value = 0.508
    noise_texture_mixing_brush_node.inputs['Roughness'].default_value = 0.0
    noise_texture_uneven_brush_node.inputs['Distortion'].default_value = 0.5
    noise_texture_mixing_brush_node.inputs['Distortion'].default_value = 0.0
    color_ramp_highlights_node.color_ramp.elements[0].position = 0.764
    color_ramp_highlights_node.color_ramp.elements[1].position = 1.0
    color_ramp_shadows_node.color_ramp.elements[0].position = 0.0
    color_ramp_shadows_node.color_ramp.elements[1].position = 1.0    
    highlights_mix_colour_node.blend_type = "OVERLAY"
    color_ramp_highlights_node.color_ramp.interpolation = 'B_SPLINE'
    color_ramp_shadows_node.color_ramp.interpolation = 'B_SPLINE'
    map_vector_gradient_highlights_node.inputs['Rotation'].default_value = (0.0, 1.5708, 0.0)
    map_vector_gradient_shadows_node.inputs['Rotation'].default_value = (0.0, 1.5708, 0.0)
    math_subtract_node_shadows.inputs[1].default_value = 0.05
    math_subtract_node_shadows.operation = "SUBTRACT"
    math_multiply_node_highlights.inputs[1].default_value = 0.95
    math_multiply_node_highlights.operation = 'MULTIPLY'
    noise_texture_mixing_brush_node.inputs['Roughness'].default_value = 0.5
    noise_texture_uneven_brush_node.inputs['Distortion'].default_value = 0.0
    
    # Set the RGB Curve Values
    curve_c = rgb_curves_node.mapping.curves[3]
    
    '''
        # Add three points at (1,1) so they're created with [2],[3] and [4] indexes
        curve_c.points.new(1,1)
        curve_c.points.new(1,1)
        curve_c.points.new(1,1)

        # Move the new points to desired (x,y) locations
        curve_c.points[2].location = (int(point1x), int(point1y))
        curve_c.points[3].location = (int(point2x), int(point2y))
        curve_c.points[4].location = (int(point3x), int(point3y))

        # Update curve. Now new points are [1],[2],[3] and last one is [4]
        rgb_curves_node.mapping.update()
    '''
    # Add three points at (0,0) so they're created with [0],[1] and [2] indexes
    #curve_c.points.new(0,0)
    #curve_c.points.new(0,0)
    #curve_c.points.new(0,0)

    # Move the new points to desired (x,y) locations
    #curve_c.points[0].location = (point1x, point1y)
    #curve_c.points[1].location = (point2x, point2y)
    #curve_c.points[2].location = (point3x, point3y)

    # Update curve. Now new points are [0],[1],[2] and last one is [3]
    rgb_curves_node.mapping.update()
    
    return watercolor_bsdf_group






def create_toon_shader(Context, operator, group_name):
    """Creates a Toon Shader that can be used"""
    
    # Create the new toon shader and give it a custom name
    bpy.context.scene.use_nodes = True

    # Create a new node group
    toon_bsdf_group = bpy.data.node_groups.new(name=TOON_BSDF_NAME, type="ShaderNodeTree")

    # Create the nodes
    group_in_node = toon_bsdf_group.nodes.new(type='NodeGroupInput')
    diffuse_bsdf_node = toon_bsdf_group.nodes.new(type="ShaderNodeBsdfDiffuse")
    glossy_bsdf_node = toon_bsdf_group.nodes.new(type="ShaderNodeBsdfGlossy")
    mix_shader_node = toon_bsdf_group.nodes.new(type="ShaderNodeMixShader")
    geometry_node = toon_bsdf_group.nodes.new(type="ShaderNodeNewGeometry")
    light_path_node = toon_bsdf_group.nodes.new(type="ShaderNodeLightPath")
    color_ramp_node = toon_bsdf_group.nodes.new(type="ShaderNodeValToRGB")
    output_node = toon_bsdf_group.nodes.new(type="NodeGroupOutput")
    toon_bsdf_shader_blender = toon_bsdf_group.nodes.new(type='ShaderNodeBsdfToon')
    normal_map_node = toon_bsdf_group.nodes.new(type='ShaderNodeNormal')


    # Set node names
    diffuse_bsdf_node.name = "Diffuse BSDF"
    glossy_bsdf_node.name = "Glossy BSDF"
    mix_shader_node.name = "Mix Shader"
    geometry_node.name = "Geometry"
    light_path_node.name = "Light Path"
    color_ramp_node.name = "Color Ramp"
    output_node.name = "Output"

    # Create the Inputs and Outputs of the group
    toon_bsdf_group.inputs.new('NodeSocketColor', 'Color')
    toon_bsdf_group.inputs['Color'].default_value = (1, 1, 1, 1)
    toon_bsdf_group.inputs.new('NodeSocketFloat', 'Diff Roughness')
    toon_bsdf_group.inputs['Diff Roughness'].default_value = 0.0
    toon_bsdf_group.inputs.new('NodeSocketFloat', 'Gloss Roughness')
    toon_bsdf_group.inputs['Gloss Roughness'].default_value = 0.5
    toon_bsdf_group.outputs.new('NodeSocketShader', 'Surface')
    

    # Connect the nodes
    toon_bsdf_group.links.new(geometry_node.outputs['Incoming'], glossy_bsdf_node.inputs['Normal'])
    toon_bsdf_group.links.new(light_path_node.outputs['Is Camera Ray'], mix_shader_node.inputs['Fac'])
    toon_bsdf_group.links.new(diffuse_bsdf_node.outputs['BSDF'], mix_shader_node.inputs[1])
    toon_bsdf_group.links.new(glossy_bsdf_node.outputs['BSDF'], mix_shader_node.inputs[2])
    toon_bsdf_group.links.new(mix_shader_node.outputs['Shader'], output_node.inputs['Surface'])
    toon_bsdf_group.links.new(light_path_node.outputs['Is Camera Ray'], color_ramp_node.inputs['Fac'])
    toon_bsdf_group.links.new(color_ramp_node.outputs['Color'], mix_shader_node.inputs['Fac'])
    toon_bsdf_group.links.new(group_in_node.outputs['Diff Roughness'], diffuse_bsdf_node.inputs['Roughness'])
    toon_bsdf_group.links.new(group_in_node.outputs['Gloss Roughness'], glossy_bsdf_node.inputs['Roughness'])
    
    
    ## Scrap the work until I find a better toon shader. Just use Toon BSDF from blender
    toon_bsdf_group.links.new(normal_map_node.outputs['Normal'], toon_bsdf_shader_blender.inputs['Normal'])
    toon_bsdf_group.links.new(toon_bsdf_shader_blender.outputs['BSDF'], output_node.inputs['Surface'])
    toon_bsdf_group.links.new(group_in_node.outputs['Color'], toon_bsdf_shader_blender.inputs['Color'])


    # Setup the toon shader as necessary
    toon_bsdf_shader_blender.inputs['Smooth'].default_value = 1.0
    toon_bsdf_shader_blender.inputs['Size'].default_value = 0.577

    # Set up the color ramp
    color_ramp_node.color_ramp.elements.new(0.2)
    color_ramp_node.color_ramp.elements[0].color = (1, 1, 1, 1)
    color_ramp_node.color_ramp.elements.new(0.5)
    color_ramp_node.color_ramp.elements[1].color = (0.5, 0.5, 0.5, 1)
    color_ramp_node.color_ramp.elements.new(0.8)
    color_ramp_node.color_ramp.elements[2].color = (0.2, 0.2, 0.2, 1)
        
    
    # Arrange in a grid for ... reasons
    num_rows = 5
    num_cols = 5
    
        
    for index, node in enumerate(toon_bsdf_group.nodes):
        # Calculate the position of the node based on its index
        row_index = index // num_cols
        col_index = index % num_cols
        x = NODE_SPACING * (col_index - 0.5 * (num_cols - 1))
        y = NODE_SPACING * (row_index - 0.5 * (num_rows - 1))

        # Set the location of the node
        node.location = (x, y)
        
    return toon_bsdf_group



""" These are the Geometry Node Functions that are necessary"""
def create_ridgid_crystal_geometry_node_group():
    # Create a new node group
    crystal_modifier = bpy.data.node_groups.new("RidgidCrystalGeometryNode", "GeometryNodeTree")

    # Create the input and output nodes
    #input_node = node_group.nodes.new('NodeGroupInput')
    #output_node = node_group.nodes.new('NodeGroupOutput')

    # Create the rest of the nodes and set their properties
    input_node = crystal_modifier.nodes.new('NodeGroupInput')
    output_node = crystal_modifier.nodes.new('NodeGroupOutput')
    #input_socket = input_node.outputs.new('NodeSocketGeometry', 'Geometry')
    #output_socket = output_node.inputs.new('NodeSocketGeometry', 'Geometry')
    input_node.name = "MyInputNode"
    output_node.name = "MyOutputNode"
    input_node.location = (-1400, 0)
    output_node.location = (2200, 0)
        
    base_mesh_node = crystal_modifier.nodes.new('GeometryNodeMeshCylinder')
    base_mesh_node.name = "MyBaseCylinderMesh"
    base_mesh_node.location = (-600, 0)

    extrude_base_mesh_node = crystal_modifier.nodes.new('GeometryNodeExtrudeMesh')
    extrude_base_mesh_node.name = "ExtrudeBaseMesh"

    scale_base_mesh_node = crystal_modifier.nodes.new('GeometryNodeScaleElements')
    scale_base_mesh_node.name = "ScaleBaseModifier"
    scale_base_mesh_node.location = (200, 0)

    boolean_base_mesh_node = crystal_modifier.nodes.new('FunctionNodeBooleanMath')
    boolean_base_mesh_node.name = "BooleanBaseMeth"
    boolean_base_mesh_node.location = (-300, -200)

    merge_by_distance_new_mesh = crystal_modifier.nodes.new('GeometryNodeMergeByDistance')
    merge_by_distance_new_mesh.name = "MergeMeshForNewMesh"
    merge_by_distance_new_mesh.location = (400, 0)

    first_dual_mesh_node = crystal_modifier.nodes.new('GeometryNodeDualMesh')
    first_dual_mesh_node.name = "FirstDualMeshNode"
    first_dual_mesh_node.location = (600, 0)
        
    second_dual_mesh_node = crystal_modifier.nodes.new('GeometryNodeDualMesh')
    second_dual_mesh_node.name = "SecondDualMeshNode"
    second_dual_mesh_node.location = (1000, 0)

    triangulate_mesh_node = crystal_modifier.nodes.new('GeometryNodeTriangulate')
    triangulate_mesh_node.name = "MeshTriangulation"
    triangulate_mesh_node.location = (800, 0)

    subdivide_mesh_node = crystal_modifier.nodes.new('GeometryNodeSubdivideMesh')
    subdivide_mesh_node.name = 'SubdivideFinalMesh'
    subdivide_mesh_node.location = (1200, 0)

    shade_smooth_final_node = crystal_modifier.nodes.new('GeometryNodeSetShadeSmooth')
    shade_smooth_final_node.name = 'FinalSmoothShade'
    shade_smooth_final_node.location = (2000, 0)


    set_material_node = crystal_modifier.nodes.new('GeometryNodeSetMaterial')
    set_material_node.name = 'SetCrystalMaterialNode'
    set_material_node.location = (1800, 0)


    set_position_node = crystal_modifier.nodes.new('GeometryNodeSetPosition')
    set_position_node.name = 'DisplacementPositionNode'
    set_position_node.location = (1600, 0)


    crystal_geometry_texture_math_node = crystal_modifier.nodes.new('ShaderNodeVectorMath')
    crystal_geometry_texture_math_node.name = 'GeometryTextureScale'
    crystal_geometry_texture_math_node.location = (1400, -200)

    crystal_geometry_texture_range_node = crystal_modifier.nodes.new('ShaderNodeMapRange')
    crystal_geometry_texture_range_node.name = 'GeometryTextureMapRange'
    crystal_geometry_texture_range_node.location = (1200, -200)


    crystal_geometry_texture_displacement_node = crystal_modifier.nodes.new('ShaderNodeTexMusgrave')
    crystal_geometry_texture_displacement_node.name = 'GeometryTextureDisplacement'
    crystal_geometry_texture_displacement_node.location = (1000, -200)

    # Set some default settings of the nodes
    base_mesh_node.inputs[0].default_value = 6
    boolean_base_mesh_node.operation = 'NOT'
    scale_base_mesh_node.inputs['Scale'].default_value = 0
    crystal_geometry_texture_math_node.operation = 'SCALE'
    crystal_geometry_texture_range_node.data_type = 'FLOAT_VECTOR' 
    crystal_geometry_texture_range_node.interpolation_type = 'LINEAR' #LINEAR #STEPPED #SMOOTHERSTEP #SMOOTHSTEP
    crystal_geometry_texture_displacement_node.musgrave_type = 'RIDGED_MULTIFRACTAL'
    crystal_geometry_texture_displacement_node.musgrave_dimensions = '4D'

    # Connect the output node to the base mesh node
    #           crystal_modifier.links.new()
    crystal_modifier.links.new(base_mesh_node.outputs['Mesh'], extrude_base_mesh_node.inputs['Mesh'])
    crystal_modifier.links.new(extrude_base_mesh_node.outputs['Mesh'], scale_base_mesh_node.inputs['Geometry'])
    crystal_modifier.links.new(extrude_base_mesh_node.outputs['Mesh'], scale_base_mesh_node.inputs['Geometry'])
    crystal_modifier.links.new(base_mesh_node.outputs['Side'], boolean_base_mesh_node.inputs['Boolean'])
    crystal_modifier.links.new(boolean_base_mesh_node.outputs['Boolean'], extrude_base_mesh_node.inputs['Selection'])
    crystal_modifier.links.new(extrude_base_mesh_node.outputs['Top'], scale_base_mesh_node.inputs['Selection'])
    crystal_modifier.links.new(second_dual_mesh_node.outputs['Dual Mesh'], subdivide_mesh_node.inputs['Mesh'])
    crystal_modifier.links.new(scale_base_mesh_node.outputs['Geometry'], merge_by_distance_new_mesh.inputs['Geometry'])
    crystal_modifier.links.new(merge_by_distance_new_mesh.outputs['Geometry'], first_dual_mesh_node.inputs['Mesh'] )
    crystal_modifier.links.new(first_dual_mesh_node.outputs['Dual Mesh'], triangulate_mesh_node.inputs['Mesh'] )
    crystal_modifier.links.new(second_dual_mesh_node.outputs['Dual Mesh'], output_node.inputs['Geometry'] )
    crystal_modifier.links.new(triangulate_mesh_node.outputs['Mesh'], second_dual_mesh_node.inputs['Mesh'])
    crystal_modifier.links.new(subdivide_mesh_node.outputs['Mesh'], set_position_node.inputs['Geometry'])
    crystal_modifier.links.new(set_position_node.outputs['Geometry'] , set_material_node.inputs['Geometry'])
    crystal_modifier.links.new(set_material_node.outputs['Geometry']  , shade_smooth_final_node.inputs['Geometry'])
    crystal_modifier.links.new(shade_smooth_final_node.outputs['Geometry'], output_node.inputs['Geometry'])

    crystal_modifier.links.new(crystal_geometry_texture_math_node.outputs['Vector'], set_position_node.inputs['Offset'])
    crystal_modifier.links.new(crystal_geometry_texture_range_node.outputs['Vector'], crystal_geometry_texture_math_node.inputs['Vector'])
    crystal_modifier.links.new(crystal_geometry_texture_displacement_node.outputs[0], crystal_geometry_texture_range_node.inputs['Vector'])

    # Return the node group
    return crystal_modifier


"""These are extra functions necessary to keep the addon working"""
def hex_to_python_tuples(hex_input_strings):
    """This function will convert hex codes to tuples that have values between 0 and 1"""
    rgba_list = []
    MAX_VALUE = 255.0
    MIN_VALUE = 1
    for hex_code in hex_input_strings:
        hex_code = hex_code + "FF"
        rgb_tuple = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4, 6))  # Convert hex code to RGB tuple
        rgba_tuple = tuple([round(c / MAX_VALUE, 3) for c in rgb_tuple])  # Convert RGB tuple to RGBA tuple with values between 0 and 1
        rgba_list.append(rgba_tuple)
    return rgba_list

def hex_to_rgb(h,alpha=1):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)] + [alpha])

def srgb_to_linearrgb(c):
    if   c < 0:       return 0
    elif c < 0.04045: return c/12.92
    else:             return ((c+0.055)/1.055)**2.4







"""This Ensures the Panel shows up in blender"""
def register():
    
    bpy.utils.register_class(AshenShadersPanel_View3D)
    bpy.utils.register_class(AshenShadersPanel_ShadersEditor)
    bpy.utils.register_class(AsenShadersPanel_RockSubMenu)
    bpy.utils.register_class(SHADER_OT_SIMPLE_TOON_BSDF)
    
    # The WC Rock Textures
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_SILVER)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_BROWN)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_BLUE)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_RED)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_BLACK)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_EMERALD)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_MAGIC)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_SAPPHIRE)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_GRASSY)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_JADE)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_TURTLE)
    
    
    # The WC Ground Textures
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_SUMMER)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_AUTUMN)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_WINTER)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_DIRT)
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_GRASS_DIRT)
    
    # The WC Tree Textures
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_NORMAL_TREE)
    
    # The WC Water Textures
    bpy.utils.register_class(SHADER_OT_WATERCOLOUR_NORMAL_WATER)
    
    
    
    
    # Geometry Nodes
    bpy.utils.register_class(SimpleGeometryNodeOperator)
    
def unregister():
    bpy.utils.unregister_class(AshenShadersPanel_View3D)
    bpy.utils.unregister_class(AshenShadersPanel_ShadersEditor)
    bpy.utils.unregister_class(AsenShadersPanel_RockSubMenu)
    bpy.utils.unregister_class(SHADER_OT_SIMPLE_TOON_BSDF)
    
    # The WC Rock Textures
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_SILVER)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_BROWN)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_BLUE)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_RED)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_BLACK)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_EMERALD)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_MAGIC)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_SAPPHIRE)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_GRASSY)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_JADE)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_TURTLE)
    
    # The WC Ground Textures
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_SUMMER)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_AUTUMN)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_WINTER)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_DIRT)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_GRASS_DIRT)
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_NORMAL_TREE)
    
    # The WC Tree Textures
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_NORMAL_TREE)
    
    # The WC Water Textures
    bpy.utils.unregister_class(SHADER_OT_WATERCOLOUR_NORMAL_WATER)





    # Geometry Nodes
    bpy.utils.unregister_class(SimpleGeometryNodeOperator)

if __name__ == "__main__":
    register()

