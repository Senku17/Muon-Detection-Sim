#Draft1
import numpy as np

#Const

D_det=1170.0
D_gen= D_det+80.0

H_det=360.0
H_gen=720.0
#GENRATION VOLUME

R_gen=D_gen/2.0
gen_z_max=H_gen/2.0
gen_z_min=-H_gen/2.0

#DETECTION VOLUME

R_det=D_det/2.0
det_z_max=H_det/2.0
det_z_min=-H_det/2.0

#array set up

mu_position= np.empty((0,3))
mu_direction=np.empty((0,3))

print("Space initialized.")
print(f"Generation Volume bounds: Z ranges from {gen_z_min}m to {gen_z_max}m, Max Radius: {R_gen}m")
print(f"Detector Volume bounds: Z ranges from {det_z_min}m to {det_z_max}m, Max Radius: {R_det}m")

