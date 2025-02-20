from header_postfx import *

####################################################################################################################
#  Each postfx_param contains the following fields:
#  1) id (string): 
#  2) flags (int). 
#  3) tonemap operator type (0,1,2,3)
#  4) shader parameters1 [ HDRRange, HDRExposureScaler, LuminanceAverageScaler, LuminanceMaxScaler ]
#  5) shader parameters2 [ BrightpassTreshold, BrightpassPostPower, BlurStrenght, BlurAmount ]
#  6) shader parameters3 [ AmbientColorCoef, SunColorCoef, SpecularCoef, -reserved ]
# 
	#define postfxParams1	(PFX1)	float4(postfx_editor_vector[1].x, postfx_editor_vector[1].y, postfx_editor_vector[1].z, postfx_editor_vector[1].w) 
	#define postfxParams2	(PFX2)	float4(postfx_editor_vector[2].x, postfx_editor_vector[2].y, postfx_editor_vector[2].z, postfx_editor_vector[2].w)
	#define postfxParams3	(PFX3)	float4(postfx_editor_vector[3].x, postfx_editor_vector[3].y, postfx_editor_vector[3].z, postfx_editor_vector[3].w)

####################################################################################################################

postfx_params = [
 ("default", 0, 0, [125.9922, 1.0588, 1.4510, 9.1765], [0.9608, 1.1373, 1.1373, 0.1961], [1.0, 1.0, 1.0, 1.0000]),
 ("map_params", 0, 3, [128.0000, 1.04, 1.2941, 10.0000], [2.3725, 2.1569, 1.8431, 0.4863], [1.0, 1.0, 1.05, 1.0]),
 ("indoors", 0, 0, [128.0000, 1.0, 1.2549, 10.0000], [0.6471, 4.7843, 4.1616, 0.00155], [0.9804, 0.9804, 1.5294, 1.0000]),
 ("sunset", 0,  0, [128.0000, 0.5882, 0.9804, 0.9804], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1.7647, 1.0000]),
 ("night", 0, 0, [128.0000, 1.0, 1.2549, 10.0000], [0.6471, 4.7843, 1.2157, 0.0000], [0.9804, 0.9804, 1.5294, 1.0000]),
 ("sunny", 0,  0, [128.0000, 0.5882, 0.9804, 0.9804], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1.7647, 1.0000]),
 ("cloudy", 0,  0, [128.0000, 0.5882, 1.04, 1.04], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1.5647, 1.0000]),
 ("overcast", 0, 0, [128.0000, 1.0, 0.9804, 0.0000], [0.3137, 2.6667, 2.0000, 0.0], [0.9804, 0.9804, 1.0314, 1.0000]) ,
 ("heavy_cloudy", 0,  0, [128.0000, 0.5882, 1.2, 1.5], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1, 1.0000]),
 ("heavy_cloudy_dark", 0,  0, [128.0000, 0.7, 1.35, 1.7], [0.1784, 3.1176, 1.3725, 0.1255], [0.9804, 0.9804, 0.8, 1.0000]),
 ("sunset_dark", 0,  0, [128.0000, 0.5882, 1.2, 1.5], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1.7647, 1.0000]),
 ("evening_clear", 0,  0, [128.0000, 0.5882, 1.04, 1.04], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1.5647, 1.0000]),
 ("evening_cloudy", 0,  0, [128.0000, 0.5882, 1.2, 1.5], [0.0784, 2.1176, 1.3725, 0.1255], [0.9804, 0.9804, 1.5647, 1.0000]),
 ("dusk_clear", 0,  0, [128.0000, 0.7, 1.5, 2], [0.25, 3.5176, 1.2725, 0.0555], [0.9804, 0.9804, 0.9, 1.0000]),
 ("dusk_cloudy", 0,  0, [128.0000, 0.7, 1.75, 2.25], [0.25, 3.5176, 1.2725, 0.0555], [0.9804, 0.9804, 0.9, 1.0000]),
 
 
 ("high_contrast", 0, 3, [128.0000, 1.0000, 1.2941, 10.0000], [0.4314, 2.0000, 1.0588, 0.0549], [2.0000, 0.7059, 1.4902, 1.0000]), 
  ]



  # modmerger_start version=201 type=4
try:
    component_name = "postfx"
    var_set = { "postfx_params":postfx_params, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
