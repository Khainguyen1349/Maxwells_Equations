import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scsp #import jv,jvp, yv,yvp, jnjnp_zeros, jnp_zeros
import plotly.graph_objects as go

def plot_cavity_field_3D(EX, EY, EZ, HX, HY, HZ, X, Y, Z, r_cavity, h_cavity, m, n, p, f0, scale_E = 1.5, scale_H = 2):
    # Circle parameters
    center_bottom = np.array([0, 0, 0])
    center_top = np.array([0, 0, h_cavity])
    theta = np.linspace(0, 2 * np.pi, 101)

    # Circle in XY plane
    bottom_circle_x = center_bottom[0] + r_cavity * np.cos(theta)
    bottom_circle_y = center_bottom[1] + r_cavity * np.sin(theta)
    bottom_circle_z = np.full_like(bottom_circle_x, center_bottom[2])  # constant z for XY plane

    top_circle_x = center_top[0] + r_cavity * np.cos(theta)
    top_circle_y = center_top[1] + r_cavity * np.sin(theta)
    top_circle_z = np.full_like(bottom_circle_x, center_top[2])  # constant z for XY plane
    
    X_flatten = X.flatten()
    Y_flatten = Y.flatten()
    Z_flatten = Z.flatten()

    flatten_ind = (X_flatten**2 + Y_flatten**2) <= r_cavity**2
    X_flatten = X_flatten[flatten_ind]
    Y_flatten = Y_flatten[flatten_ind]
    Z_flatten = Z_flatten[flatten_ind]
    
    E_X_flatten = EX.flatten()[flatten_ind]
    E_Y_flatten = EY.flatten()[flatten_ind]
    E_Z_flatten = EZ.flatten()[flatten_ind]
    
    H_X_flatten = HX.flatten()[flatten_ind]
    H_Y_flatten = HY.flatten()[flatten_ind]
    H_Z_flatten = HZ.flatten()[flatten_ind]
    
    fig1 = go.Figure(data = go.Cone(
        x=X_flatten,
        y=Y_flatten,
        z=Z_flatten,
        u=E_X_flatten,
        v=E_Y_flatten,
        w=E_Z_flatten,
        colorscale='Reds',
        sizemode="absolute",
        sizeref=scale_E*np.sqrt(E_X_flatten**2 +E_Y_flatten**2 + E_Z_flatten**2).max()))


    fig1.add_trace(go.Scatter3d(x=bottom_circle_x,
                               y=bottom_circle_y,
                               z=bottom_circle_z,
                               mode='lines',
                               line=dict(color='black', width=4),
                               showlegend=False))
    fig1.add_trace(go.Scatter3d(x=top_circle_x,
                               y=top_circle_y,
                               z=top_circle_z,
                               mode='lines',
                               line=dict(color='black', width=4),
                               showlegend=False))
    for i in range(10):
        fig1.add_trace(go.Scatter3d(x=[r_cavity*np.cos(2*i*np.pi/10), r_cavity*np.cos(2*i*np.pi/10)],
                                   y=[r_cavity*np.sin(2*i*np.pi/10), r_cavity*np.sin(2*i*np.pi/10)],
                                   z=[0, h_cavity],
                                   mode='lines',
                                   line=dict(color='black'),
                                   showlegend=False))

    fig1.update_layout(width=900, height=800, title=f"E-Field mode TE{m}{n}{p}, f_c = {np.round(f0/1e9,2)} GHz",
                       scene=dict(aspectratio=dict(x=1, y=1, z=0.8),
                                 camera_eye=dict(x=1.2, y=1.2, z=0.6)))
    fig1.show()

    fig2 = go.Figure(data = go.Cone(
        x=X_flatten,
        y=Y_flatten,
        z=Z_flatten,
        u=H_X_flatten,
        v=H_Y_flatten,
        w=H_Z_flatten,
        colorscale='Blues',
        sizemode="absolute",
        sizeref=scale_H*np.sqrt(H_X_flatten**2 +H_Y_flatten**2 + H_Z_flatten**2).max()))

    fig2.add_trace(go.Scatter3d(x=bottom_circle_x,
                               y=bottom_circle_y,
                               z=bottom_circle_z,
                               mode='lines',
                               line=dict(color='black', width=4),
                               showlegend=False))
    fig2.add_trace(go.Scatter3d(x=top_circle_x,
                               y=top_circle_y,
                               z=top_circle_z,
                               mode='lines',
                               line=dict(color='black', width=4),
                               showlegend=False))
    for i in range(10):
        fig2.add_trace(go.Scatter3d(x=[r_cavity*np.cos(2*i*np.pi/10), r_cavity*np.cos(2*i*np.pi/10)],
                                   y=[r_cavity*np.sin(2*i*np.pi/10), r_cavity*np.sin(2*i*np.pi/10)],
                                   z=[0, h_cavity],
                                   mode='lines',
                                   line=dict(color='black'),
                                   showlegend=False))

    fig2.update_layout(width=900, height=800, title=f"H-Field mode TE{m}{n}{p}, f_c = {np.round(f0/1e9,2)} GHz",
                       scene=dict(aspectratio=dict(x=1, y=1, z=0.8),
                                 camera_eye=dict(x=1.2, y=1.2, z=0.6)))
    fig2.show()
    
    
def plot_cavity_field_2D(EX, EY, EZ, HX, HY, HZ, X, Y, Z, r_cavity, h_cavity, z_index_observation):
    npoint = len(Z[0,0,:])
    max_E = np.sqrt(EX**2 + EY**2 + EZ**2).max()
    max_H = np.sqrt(HX**2 + HY**2 + HZ**2).max()
    # Create 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    # Top-left
    circle1 = plt.Circle((0, 0), r_cavity, color='y', fill=0, linewidth = 5)
    axes[0, 0].add_patch(circle1)

    q1 = axes[0, 0].pcolormesh(X[:,:,0], Y[:,:,0], 
                               np.sqrt(EX[:,:,z_index_observation]**2 + EY[:,:,z_index_observation]**2 + EZ[:,:,z_index_observation]**2),
                               cmap='Reds', shading='gouraud')
    fig.colorbar(q1, ax=axes[0, 0])
    q2 = axes[0, 0].quiver(X[:,:,0], Y[:,:,0], EX[:,:,z_index_observation], EY[:,:,z_index_observation],
                            scale=max_E*20)
    axes[0, 0].quiverkey(q2, X=0.3, Y=1.1, U=1,
                 label='', labelpos='E')
    axes[0, 0].set_title(f"E_field @z=L/{round(h_cavity/Z[0,0,z_index_observation])}")

    # Top-right
    q3 = axes[0, 1].pcolormesh(X[:,0,:], Z[:,0,:], np.sqrt(EX[:,int(npoint/2),:]**2 + EY[:,int(npoint/2),:]**2 + EZ[:,int(npoint/2),:]**2), 
                               cmap='Reds', shading='gouraud')
    fig.colorbar(q3, ax=axes[0, 1])

    q4 = axes[0, 1].quiver(X[:,0,:], Z[:,0,:], EX[:,int(npoint/2),:], EZ[:,int(npoint/2),:], scale=max_E*20)
    axes[0, 1].quiverkey(q4, X=0.3, Y=1.1, U=1,
                 label='', labelpos='E')
    axes[0, 1].set_title("E_field @y=0")

    # Bottom-left
    circle1 = plt.Circle((0, 0), r_cavity, color='y', fill=0, linewidth = 5)
    axes[1, 0].add_patch(circle1)

    q5 = axes[1, 0].pcolormesh(X[:,:,0], Y[:,:,0], 
                               np.sqrt(HX[:,:,z_index_observation]**2 + HY[:,:,z_index_observation]**2 + HZ[:,:,z_index_observation]**2),
                               cmap='Blues', shading='gouraud')
    fig.colorbar(q5, ax=axes[1, 0])

    q6 = axes[1, 0].quiver(X[:,:,0], Y[:,:,0], HX[:,:,z_index_observation], HY[:,:,z_index_observation], scale=max_H*20)
    axes[1, 0].quiverkey(q6, X=0.3, Y=1.1, U=100,
                 label='', labelpos='E')
    axes[1, 0].set_title(f"H_field @z=L/{round(h_cavity/Z[0,0,z_index_observation])}")

    # Bottom-right
    q7 = axes[1, 1].pcolormesh(X[:,0,:], Z[:,0,:], 
                               np.sqrt(HX[:,int(npoint/2),:]**2 + HY[:,int(npoint/2),:]**2 + HZ[:,int(npoint/2),:]**2), 
                               cmap='Blues', shading='gouraud')
    fig.colorbar(q7, ax=axes[1, 1])

    q8 = axes[1, 1].quiver(X[:,0,:], Z[:,0,:], HX[:,int(npoint/2),:], HZ[:,int(npoint/2),:], scale=max_H*20)
    axes[1, 1].quiverkey(q8, X=0.3, Y=1.1, U=1,
                 label='', labelpos='E')
    axes[1, 1].set_title("H_field @y=0")

    # Automatically adjust spacing
    fig.tight_layout()

    plt.show()