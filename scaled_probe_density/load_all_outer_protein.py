from pymol import cmd

# Function to set higher-resolution settings for rendering
def set_high_quality_settings():
    cmd.set("antialias", 2)  # Increase antialiasing for smoother lines
    cmd.set("orthoscopic", 1)  # Use orthoscopic projection for better quality
    cmd.set("spec_reflect", 0)  # Enable specular reflection
    cmd.set("ambient", 0.1)  # Adjust ambient light
    cmd.set("direct", 0.65)  # Adjust direct light
    cmd.set("ray_trace_fog", 1)  # Disable fog for ray tracing
    cmd.set("ray_shadow_decay_factor", 0)  # Reduce shadow decay for better shadows, create shadows in the cavity
    cmd.set("depth_cue", 1)
    cmd.set("ray_shadow", 0)

set_high_quality_settings()

# Load the protein structure
cmd.load('IRF3_IMI.pdb')

# Create two separate representations for the surface and the cartoon
cmd.create('surface_obj', 'IRF3_IMI')
cmd.create('cartoon_obj', 'IRF3_IMI')

# Show and style the surface
cmd.show('surface', 'surface_obj')
cmd.color('white', 'surface_obj')
cmd.set('transparency', 0.12, 'surface_obj')

# Show and style the cartoon
cmd.show('cartoon', 'cartoon_obj')
cmd.color('green', 'cartoon_obj')

# Load and display the isomesh files
cmd.load('out_align_IMI_1P3_scaled.xplor')
cmd.isomesh('IMI_mesh', 'out_align_IMI_1P3_scaled', level=70)
cmd.color('red', 'IMI_mesh')
cmd.set("mesh_width", 1.5, 'IMI_mesh')

cmd.load('out_align_1P3_1P3_scaled.xplor')
cmd.isomesh('1P3_mesh', 'out_align_1P3_1P3_scaled', level=70)
cmd.color('green', '1P3_mesh')
cmd.set("mesh_width", 1.5, '1P3_mesh')

cmd.load('out_align_C3N_1P3_scaled.xplor')
cmd.isomesh('C3N_mesh', 'out_align_C3N_1P3_scaled', level=70)
cmd.color('blue', 'C3N_mesh')
cmd.set("mesh_width", 1.5, 'C3N_mesh')

cmd.load('out_align_EOH_1P3_scaled.xplor')
cmd.isomesh('EOH_mesh', 'out_align_EOH_1P3_scaled', level=70)
cmd.color('black', 'EOH_mesh')
cmd.set("mesh_width", 1.5, 'EOH_mesh')

cmd.load('out_align_IPA_1P3_scaled.xplor')
cmd.isomesh('IPA_mesh', 'out_align_IPA_1P3_scaled', level=70)
cmd.color('cyan', 'IPA_mesh')
cmd.set("mesh_width", 1.5, 'IPA_mesh')

cmd.load('out_align_NMA_1P3_scaled.xplor')
cmd.isomesh('NMA_mesh', 'out_align_NMA_1P3_scaled', level=70)
cmd.color('magenta', 'NMA_mesh')
cmd.set("mesh_width", 1.5, 'NMA_mesh')
