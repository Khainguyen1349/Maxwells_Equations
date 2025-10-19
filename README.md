# Maxwell

To fully understand the marvels of Maxwell's equations, I deep-dived into the mathematical aspects of it throughout different case studies. 

## Cavity modes 
Let's start with the most basic example. This might help you "see" the physical phenomenon of the mathematical equations.

The first thing one may need to understand is the notion of an eigenstate (eigenvector) and an eigenvalue. It can be clear from the mathematical expressions that the eigenvector **x** and its corresponding eigenvalue &lambda; of a matrix  **A** verify **Ax** = &lambda;**x**. This means that the modifications (scale, stretch, and rotation) defined by the matrix **A** on the state **v**, represented by the parameters in the vector, do nothing special but scale the vector by a factor &lambda;.

Try to remember this **A** is the function/equation, **v** is the state. In the context of an electromagnetic field, **A** is the system defined by Maxwell's equations, and the eigen-states **v**(s) are the electric fields (Efield) and magnetic fields (Hfield). In a closed system, e.g., in a cavity with a closed border with Perfect Electrical/Magnetic Condition, the total E-/H-field can be decomposed into _discrete_ eigen-E-/H-fields.

To visualize two of the eigenstates, I have plotted beautifully one higher mode TM311 of a cylindrical cavity as follows.

### 3D EField 
<img src="https://github.com/Khainguyen1349/Maxwells_Equations/blob/main/Cylindrical_Cavity_Modes/Figures/3DElectricFieldTM311.png" width=40% height=40%>

### 3D HField 
<img src="https://github.com/Khainguyen1349/Maxwells_Equations/blob/main/Cylindrical_Cavity_Modes/Figures/3DMagneticFieldTM311.png" width=40% height=40%>

### 2D EField and HField
<img src="https://github.com/Khainguyen1349/Maxwells_Equations/blob/main/Cylindrical_Cavity_Modes/Figures/2DEHFieldTM311.png" width=60% height=60%>

## Plane-Wave Expansion (PWE)
From the previous study on the Cavity modes, one understands the meaning of "decomposition". Maxwell's equations can be applied to an "infinite" plane, and the decomposition also simplifies a lot the solution to find eigenstates of the fields. Even more interestingly, the properties of the fields defined by the equation allow translation and "propagation" of the field. The PWE explains this.

First, the procedure of decomposing the field is transforming the spatial field, the one that one can imagine easily, to a spectral one, which one might have some difficulties imagining. In a few words, the spatial vector field has a complex vector at every point in the common 3D space you see. On the other hand, a spectral field also has a complex vector at every point in its domain, but every point represents a direction, defined by (&theta;&phi;). The idea is that every angular/directional component of the spectral domain of a spatial plane preserves its magnitude when being translated to another plane in parallel with its phase adding a delay due to the propagation between the two planes. 

In the example below, I generate an electrical field radiated by an array of Hertzian dipoles at 20mm away from the array, parallel to the longitude of the array. Then this field is propagated to 100mm away from the array. Interestingly, because the spectral field is represented by the strength (and phase) of directions (&theta;&phi;), one can extract the partial radiation pattern of the antenna. 

### EField at 20mm
<img src="https://github.com/Khainguyen1349/Maxwells_Equations/blob/main/Plane_Wave_Expansion/Figures/ElectricalFieldAt20mm.png" width=60% height=60%>

### EField at 20mm
<img src="https://github.com/Khainguyen1349/Maxwells_Equations/blob/main/Plane_Wave_Expansion/Figures/ElectricalFieldAt100mm.png" width=60% height=60%>

### Radiation pattern extracted 
<img src="https://github.com/Khainguyen1349/Maxwells_Equations/blob/main/Plane_Wave_Expansion/Figures/RadiationField.png" width=60% height=60%>

## Raytracing

## Dispersion Diagram

