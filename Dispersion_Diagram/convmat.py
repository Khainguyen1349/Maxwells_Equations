import numpy as np


def convmat(A, P, Q=None, R=None):
    """
    Construct a convolution matrix from a real-space grid A.
    Supports 1D, 2D, and 3D (assumes A.ndim = 1, 2, or 3).
    """
    # Handle input arguments (1D: P, 2D: P, Q, 3D: P, Q, R)
    if Q is None:
        Q = 1
    if R is None:
        R = 1
    A = np.asarray(A)
    shape = A.shape
    Nx, Ny, Nz = 1, 1, 1
    if A.ndim == 3:
        Nx, Ny, Nz = shape
    elif A.ndim == 2:
        Nx, Ny = shape
    elif A.ndim == 1:
        Nx = shape[0]

    # Indices of spatial harmonics
    p = np.arange(-P//2, P//2+1)
    q = np.arange(-Q//2, Q//2+1)
    r = np.arange(-R//2, R//2+1)
    NH = P*Q*R
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"r = {r}")

    # Fourier coefficients of A (normalized FFT, with fftshift)
    Ahat = np.fft.fftshift(np.fft.fftn(A)) / (Nx * Ny * Nz)
    #print(f"Ahat[:,63,63] = {Ahat[64,:,63]}")
    
    # Zero-order harmonic index
    p0 = Nx//2
    q0 = Ny//2
    r0 = Nz//2
    print(f"p0 = {p0}")
    print(f"q0 = {q0}")
    print(f"r0 = {r0}")

    # Convolution matrix
    C = np.zeros((NH, NH), dtype=np.complex128)
    # For each output block (row/col index)
    rowidx = 0
    for rrow in range(R):
        for qrow in range(Q):
            for prow in range(P):
                row = rrow * Q * P + qrow * P + prow
                for rcol in range(R):
                    for qcol in range(Q):
                        for pcol in range(P):
                            col = rcol * Q * P + qcol * P + pcol
                            pfft = p[prow] - p[pcol]
                            qfft = q[qrow] - q[qcol]
                            rfft = r[rrow] - r[rcol]
                            idx_p = p0 + pfft
                            idx_q = q0 + qfft
                            idx_r = r0 + rfft
                            C[row, col] = Ahat[idx_q, idx_p, idx_r]
    return C
