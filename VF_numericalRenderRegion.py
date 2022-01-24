bl_info = {
	"name": "VF Numerical Render Region",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 2),
	"blender": (3, 0, 0),
	"location": "Rendertab > Output Panel > Subpanel",
	"description": "Adds Blender's native numerical render region settings to the render output tab",
	"warning": "inexperienced developer, use at your own risk",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Render"}

# Based on the following resources:
# https://b3d.interplanety.org/en/setting-render-border-coordinates/

import bpy

###########################################################################
# Project settings and UI rendering classes

class RENDER_PT_numerical_render_region(bpy.types.Panel):
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render"
	bl_label = "Render Region Values"
	bl_parent_id = "RENDER_PT_format"
	# bl_options = {'DEFAULT_CLOSED'}
	bl_options = {'HIDE_HEADER'}

	# def draw_header(self, context):
		# self.layout.prop(bpy.context.scene.render, 'use_border', text='')

	def draw(self, context):
		if bpy.context.scene.render.use_border:
			layout = self.layout
			layout.use_property_decorate = False  # No animation
			layout.use_property_split = True

			# row = layout.row(align=True, heading='')
			# row.prop(bpy.context.scene.render, 'border_min_y', text='Bottom | Top | Left | Right')
			# row.prop(bpy.context.scene.render, 'border_max_y', text='')
			# row.prop(bpy.context.scene.render, 'border_min_x', text='')
			# row.prop(bpy.context.scene.render, 'border_max_x', text='')

			col = layout.column(align=True)
			col.prop(bpy.context.scene.render, 'border_min_y', text='Render Region Bottom')
			col.prop(bpy.context.scene.render, 'border_max_y', text='Top')
			col.prop(bpy.context.scene.render, 'border_min_x', text='Left')
			col.prop(bpy.context.scene.render, 'border_max_x', text='Right')

###########################################################################
# Addon registration functions

def register():
	bpy.utils.register_class(RENDER_PT_numerical_render_region)

def unregister():
	bpy.utils.unregister_class(RENDER_PT_numerical_render_region)

if __name__ == "__main__":
	register()
