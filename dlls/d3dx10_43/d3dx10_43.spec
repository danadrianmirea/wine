@ stdcall D3DX10CreateThreadPump(long long ptr)
@ stdcall D3DX10CheckVersion(long long)
@ stub D3DX10CompileFromFileA(str ptr ptr str str long long ptr ptr ptr ptr)
@ stub D3DX10CompileFromFileW(wstr ptr ptr str str long long ptr ptr ptr ptr)
@ stdcall D3DX10CompileFromMemory(ptr long str ptr ptr str str long long ptr ptr ptr ptr)
@ stub D3DX10CompileFromResourceA(long str str ptr ptr str str long long ptr ptr ptr ptr)
@ stub D3DX10CompileFromResourceW(long wstr wstr ptr ptr str str long long ptr ptr ptr ptr)
@ stub D3DX10ComputeNormalMap(ptr long long long ptr)
@ stub D3DX10CreateAsyncCompilerProcessor(str ptr ptr str str long long ptr ptr ptr)
@ stub D3DX10CreateAsyncEffectCreateProcessor(str ptr ptr str long long ptr ptr ptr ptr)
@ stub D3DX10CreateAsyncEffectPoolCreateProcessor(str ptr ptr str long long ptr ptr ptr)
@ stdcall D3DX10CreateAsyncFileLoaderA(str ptr)
@ stdcall D3DX10CreateAsyncFileLoaderW(wstr ptr)
@ stdcall D3DX10CreateAsyncMemoryLoader(ptr long ptr)
@ stdcall D3DX10CreateAsyncResourceLoaderA(long str ptr)
@ stdcall D3DX10CreateAsyncResourceLoaderW(long wstr ptr)
@ stub D3DX10CreateAsyncShaderPreprocessProcessor(str ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateAsyncShaderResourceViewProcessor(ptr ptr ptr)
@ stdcall D3DX10CreateAsyncTextureInfoProcessor(ptr ptr)
@ stdcall D3DX10CreateAsyncTextureProcessor(ptr ptr ptr)
@ stdcall D3DX10CreateDevice(ptr long long long ptr)
@ stdcall D3DX10CreateDeviceAndSwapChain(ptr long long long ptr ptr ptr)
@ stdcall D3DX10CreateEffectFromFileA(str ptr ptr str long long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectFromFileW(wstr ptr ptr str long long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectFromMemory(ptr long str ptr ptr str long long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectFromResourceA(long str str ptr ptr str long long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectFromResourceW(long wstr wstr ptr ptr str long long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectPoolFromFileA(str ptr ptr str long long ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectPoolFromFileW(wstr ptr ptr str long long ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateEffectPoolFromMemory(ptr long str ptr ptr str long long ptr ptr ptr ptr ptr)
@ stub D3DX10CreateEffectPoolFromResourceA(long str str ptr ptr str long long ptr ptr ptr ptr ptr)
@ stub D3DX10CreateEffectPoolFromResourceW(long wstr wstr ptr ptr str long long ptr ptr ptr ptr ptr)
@ stdcall D3DX10CreateFontA(ptr long long long long long long long long long str ptr)
@ stdcall D3DX10CreateFontIndirectA(ptr ptr ptr)
@ stdcall D3DX10CreateFontIndirectW(ptr ptr ptr)
@ stdcall D3DX10CreateFontW(ptr long long long long long long long long long wstr ptr)
@ stdcall D3DX10CreateMesh(ptr ptr long str long long long ptr)
@ stdcall D3DX10CreateShaderResourceViewFromFileA(ptr str ptr ptr ptr ptr)
@ stdcall D3DX10CreateShaderResourceViewFromFileW(ptr wstr ptr ptr ptr ptr)
@ stdcall D3DX10CreateShaderResourceViewFromMemory(ptr ptr long ptr ptr ptr ptr)
@ stdcall D3DX10CreateShaderResourceViewFromResourceA(ptr long str ptr ptr ptr ptr)
@ stdcall D3DX10CreateShaderResourceViewFromResourceW(ptr long wstr ptr ptr ptr ptr)
@ stub D3DX10CreateSkinInfo(ptr)
@ stdcall D3DX10CreateSprite(ptr long ptr)
@ stdcall D3DX10CreateTextureFromFileA(ptr str ptr ptr ptr ptr)
@ stdcall D3DX10CreateTextureFromFileW(ptr wstr ptr ptr ptr ptr)
@ stdcall D3DX10CreateTextureFromMemory(ptr ptr long ptr ptr ptr ptr)
@ stdcall D3DX10CreateTextureFromResourceA(ptr long str ptr ptr ptr ptr)
@ stdcall D3DX10CreateTextureFromResourceW(ptr long wstr ptr ptr ptr ptr)
@ stdcall D3DX10FilterTexture(ptr long long)
@ stdcall D3DX10GetFeatureLevel1(ptr ptr)
@ stdcall D3DX10GetImageInfoFromFileA(str ptr ptr ptr)
@ stdcall D3DX10GetImageInfoFromFileW(wstr ptr ptr ptr)
@ stdcall D3DX10GetImageInfoFromMemory(ptr long ptr ptr ptr)
@ stdcall D3DX10GetImageInfoFromResourceA(long str ptr ptr ptr)
@ stdcall D3DX10GetImageInfoFromResourceW(long wstr ptr ptr ptr)
@ stdcall D3DX10LoadTextureFromTexture(ptr ptr ptr)
@ stub D3DX10PreprocessShaderFromFileA(str ptr ptr ptr ptr ptr)
@ stub D3DX10PreprocessShaderFromFileW(wstr ptr ptr ptr ptr ptr)
@ stdcall D3DX10PreprocessShaderFromMemory(ptr long str ptr ptr ptr ptr ptr ptr)
@ stub D3DX10PreprocessShaderFromResourceA(long str str ptr ptr ptr ptr ptr)
@ stub D3DX10PreprocessShaderFromResourceW(long wstr wstr ptr ptr ptr ptr ptr)
@ stub D3DX10SHProjectCubeMap(long ptr ptr ptr ptr)
@ stub D3DX10SaveTextureToFileA(ptr ptr str)
@ stub D3DX10SaveTextureToFileW(ptr ptr wstr)
@ stub D3DX10SaveTextureToMemory(ptr ptr ptr long)
@ stdcall D3DX10UnsetAllDeviceObjects(ptr)
@ stdcall D3DXBoxBoundProbe(ptr ptr ptr ptr) d3dx9_36.D3DXBoxBoundProbe
@ stdcall D3DXColorAdjustContrast(ptr ptr float) d3dx9_36.D3DXColorAdjustContrast
@ stdcall D3DXColorAdjustSaturation(ptr ptr float) d3dx9_36.D3DXColorAdjustSaturation
@ stdcall D3DXComputeBoundingBox(ptr long long ptr ptr) d3dx9_36.D3DXComputeBoundingBox
@ stdcall D3DXComputeBoundingSphere(ptr long long ptr ptr) d3dx9_36.D3DXComputeBoundingSphere
@ stdcall D3DXCpuOptimizations(long)
@ stdcall D3DXCreateMatrixStack(long ptr) d3dx9_36.D3DXCreateMatrixStack
@ stdcall D3DXFloat16To32Array(ptr ptr long) d3dx9_36.D3DXFloat16To32Array
@ stdcall D3DXFloat32To16Array(ptr ptr long) d3dx9_36.D3DXFloat32To16Array
@ stdcall D3DXFresnelTerm(float float) d3dx9_36.D3DXFresnelTerm
@ stdcall D3DXIntersectTri(ptr ptr ptr ptr ptr ptr ptr ptr) d3dx9_36.D3DXIntersectTri
@ stdcall D3DXMatrixAffineTransformation2D(ptr float ptr float ptr) d3dx9_36.D3DXMatrixAffineTransformation2D
@ stdcall D3DXMatrixAffineTransformation(ptr float ptr ptr ptr) d3dx9_36.D3DXMatrixAffineTransformation
@ stdcall D3DXMatrixDecompose(ptr ptr ptr ptr) d3dx9_36.D3DXMatrixDecompose
@ stdcall D3DXMatrixDeterminant(ptr) d3dx9_36.D3DXMatrixDeterminant
@ stdcall D3DXMatrixInverse(ptr ptr ptr) d3dx9_36.D3DXMatrixInverse
@ stdcall D3DXMatrixLookAtLH(ptr ptr ptr ptr) d3dx9_36.D3DXMatrixLookAtLH
@ stdcall D3DXMatrixLookAtRH(ptr ptr ptr ptr) d3dx9_36.D3DXMatrixLookAtRH
@ stdcall D3DXMatrixMultiply(ptr ptr ptr) d3dx9_36.D3DXMatrixMultiply
@ stdcall D3DXMatrixMultiplyTranspose(ptr ptr ptr) d3dx9_36.D3DXMatrixMultiplyTranspose
@ stdcall D3DXMatrixOrthoLH(ptr float float float float) d3dx9_36.D3DXMatrixOrthoLH
@ stdcall D3DXMatrixOrthoOffCenterLH(ptr float float float float float float) d3dx9_36.D3DXMatrixOrthoOffCenterLH
@ stdcall D3DXMatrixOrthoOffCenterRH(ptr float float float float float float) d3dx9_36.D3DXMatrixOrthoOffCenterRH
@ stdcall D3DXMatrixOrthoRH(ptr float float float float) d3dx9_36.D3DXMatrixOrthoRH
@ stdcall D3DXMatrixPerspectiveFovLH(ptr float float float float) d3dx9_36.D3DXMatrixPerspectiveFovLH
@ stdcall D3DXMatrixPerspectiveFovRH(ptr float float float float) d3dx9_36.D3DXMatrixPerspectiveFovRH
@ stdcall D3DXMatrixPerspectiveLH(ptr float float float float) d3dx9_36.D3DXMatrixPerspectiveLH
@ stdcall D3DXMatrixPerspectiveOffCenterLH(ptr float float float float float float) d3dx9_36.D3DXMatrixPerspectiveOffCenterLH
@ stdcall D3DXMatrixPerspectiveOffCenterRH(ptr float float float float float float) d3dx9_36.D3DXMatrixPerspectiveOffCenterRH
@ stdcall D3DXMatrixPerspectiveRH(ptr float float float float) d3dx9_36.D3DXMatrixPerspectiveRH
@ stdcall D3DXMatrixReflect(ptr ptr) d3dx9_36.D3DXMatrixReflect
@ stdcall D3DXMatrixRotationAxis(ptr ptr float) d3dx9_36.D3DXMatrixRotationAxis
@ stdcall D3DXMatrixRotationQuaternion(ptr ptr) d3dx9_36.D3DXMatrixRotationQuaternion
@ stdcall D3DXMatrixRotationX(ptr float) d3dx9_36.D3DXMatrixRotationX
@ stdcall D3DXMatrixRotationY(ptr float) d3dx9_36.D3DXMatrixRotationY
@ stdcall D3DXMatrixRotationYawPitchRoll(ptr float float float) d3dx9_36.D3DXMatrixRotationYawPitchRoll
@ stdcall D3DXMatrixRotationZ(ptr float) d3dx9_36.D3DXMatrixRotationZ
@ stdcall D3DXMatrixScaling(ptr float float float) d3dx9_36.D3DXMatrixScaling
@ stdcall D3DXMatrixShadow(ptr ptr ptr) d3dx9_36.D3DXMatrixShadow
@ stdcall D3DXMatrixTransformation2D(ptr ptr float ptr ptr float ptr) d3dx9_36.D3DXMatrixTransformation2D
@ stdcall D3DXMatrixTransformation(ptr ptr ptr ptr ptr ptr ptr) d3dx9_36.D3DXMatrixTransformation
@ stdcall D3DXMatrixTranslation(ptr float float float) d3dx9_36.D3DXMatrixTranslation
@ stdcall D3DXMatrixTranspose(ptr ptr) d3dx9_36.D3DXMatrixTranspose
@ stdcall D3DXPlaneFromPointNormal(ptr ptr ptr) d3dx9_36.D3DXPlaneFromPointNormal
@ stdcall D3DXPlaneFromPoints(ptr ptr ptr ptr) d3dx9_36.D3DXPlaneFromPoints
@ stdcall D3DXPlaneIntersectLine(ptr ptr ptr ptr) d3dx9_36.D3DXPlaneIntersectLine
@ stdcall D3DXPlaneNormalize(ptr ptr) d3dx9_36.D3DXPlaneNormalize
@ stdcall D3DXPlaneTransform(ptr ptr ptr) d3dx9_36.D3DXPlaneTransform
@ stdcall D3DXPlaneTransformArray(ptr long ptr long ptr long) d3dx9_36.D3DXPlaneTransformArray
@ stdcall D3DXQuaternionBaryCentric(ptr ptr ptr ptr float float) d3dx9_36.D3DXQuaternionBaryCentric
@ stdcall D3DXQuaternionExp(ptr ptr) d3dx9_36.D3DXQuaternionExp
@ stdcall D3DXQuaternionInverse(ptr ptr) d3dx9_36.D3DXQuaternionInverse
@ stdcall D3DXQuaternionLn(ptr ptr) d3dx9_36.D3DXQuaternionLn
@ stdcall D3DXQuaternionMultiply(ptr ptr ptr) d3dx9_36.D3DXQuaternionMultiply
@ stdcall D3DXQuaternionNormalize(ptr ptr) d3dx9_36.D3DXQuaternionNormalize
@ stdcall D3DXQuaternionRotationAxis(ptr ptr float) d3dx9_36.D3DXQuaternionRotationAxis
@ stdcall D3DXQuaternionRotationMatrix(ptr ptr) d3dx9_36.D3DXQuaternionRotationMatrix
@ stdcall D3DXQuaternionRotationYawPitchRoll(ptr float float float) d3dx9_36.D3DXQuaternionRotationYawPitchRoll
@ stdcall D3DXQuaternionSlerp(ptr ptr ptr float) d3dx9_36.D3DXQuaternionSlerp
@ stdcall D3DXQuaternionSquad(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXQuaternionSquad
@ stdcall D3DXQuaternionSquadSetup(ptr ptr ptr ptr ptr ptr ptr) d3dx9_36.D3DXQuaternionSquadSetup
@ stdcall D3DXQuaternionToAxisAngle(ptr ptr ptr) d3dx9_36.D3DXQuaternionToAxisAngle
@ stdcall D3DXSHAdd(ptr long ptr ptr) d3dx9_36.D3DXSHAdd
@ stdcall D3DXSHDot(long ptr ptr) d3dx9_36.D3DXSHDot
@ stdcall D3DXSHEvalConeLight(long ptr float float float float ptr ptr ptr) d3dx9_36.D3DXSHEvalConeLight
@ stdcall D3DXSHEvalDirection(ptr long ptr) d3dx9_36.D3DXSHEvalDirection
@ stdcall D3DXSHEvalDirectionalLight(long ptr float float float ptr ptr ptr) d3dx9_36.D3DXSHEvalDirectionalLight
@ stdcall D3DXSHEvalHemisphereLight(long ptr long long ptr ptr ptr) d3dx9_36.D3DXSHEvalHemisphereLight
@ stdcall D3DXSHEvalSphericalLight(long ptr long long long long ptr ptr ptr) d3dx9_36.D3DXSHEvalSphericalLight
@ stdcall D3DXSHMultiply2(ptr ptr ptr) d3dx9_36.D3DXSHMultiply2
@ stdcall D3DXSHMultiply3(ptr ptr ptr) d3dx9_36.D3DXSHMultiply3
@ stdcall D3DXSHMultiply4(ptr ptr ptr) d3dx9_36.D3DXSHMultiply4
@ stdcall D3DXSHMultiply5(ptr ptr ptr) d3dx9_36.D3DXSHMultiply5
@ stdcall D3DXSHMultiply6(ptr ptr ptr) d3dx9_36.D3DXSHMultiply6
@ stdcall D3DXSHRotate(ptr long ptr ptr) d3dx9_36.D3DXSHRotate
@ stdcall D3DXSHRotateZ(ptr long float ptr) d3dx9_36.D3DXSHRotateZ
@ stdcall D3DXSHScale(ptr long ptr float) d3dx9_36.D3DXSHScale
@ stdcall D3DXSphereBoundProbe(ptr float ptr ptr) d3dx9_36.D3DXSphereBoundProbe
@ stdcall D3DXVec2BaryCentric(ptr ptr ptr ptr float float) d3dx9_36.D3DXVec2BaryCentric
@ stdcall D3DXVec2CatmullRom(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXVec2CatmullRom
@ stdcall D3DXVec2Hermite(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXVec2Hermite
@ stdcall D3DXVec2Normalize(ptr ptr) d3dx9_36.D3DXVec2Normalize
@ stdcall D3DXVec2Transform(ptr ptr ptr) d3dx9_36.D3DXVec2Transform
@ stdcall D3DXVec2TransformArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec2TransformArray
@ stdcall D3DXVec2TransformCoord(ptr ptr ptr) d3dx9_36.D3DXVec2TransformCoord
@ stdcall D3DXVec2TransformCoordArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec2TransformCoordArray
@ stdcall D3DXVec2TransformNormal(ptr ptr ptr) d3dx9_36.D3DXVec2TransformNormal
@ stdcall D3DXVec2TransformNormalArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec2TransformNormalArray
@ stdcall D3DXVec3BaryCentric(ptr ptr ptr ptr float float) d3dx9_36.D3DXVec3BaryCentric
@ stdcall D3DXVec3CatmullRom(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXVec3CatmullRom
@ stdcall D3DXVec3Hermite(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXVec3Hermite
@ stdcall D3DXVec3Normalize(ptr ptr) d3dx9_36.D3DXVec3Normalize
@ stdcall D3DXVec3Project(ptr ptr ptr ptr ptr ptr) d3dx9_36.D3DXVec3Project
@ stdcall D3DXVec3ProjectArray(ptr long ptr long ptr ptr ptr ptr long) d3dx9_36.D3DXVec3ProjectArray
@ stdcall D3DXVec3Transform(ptr ptr ptr) d3dx9_36.D3DXVec3Transform
@ stdcall D3DXVec3TransformArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec3TransformArray
@ stdcall D3DXVec3TransformCoord(ptr ptr ptr) d3dx9_36.D3DXVec3TransformCoord
@ stdcall D3DXVec3TransformCoordArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec3TransformCoordArray
@ stdcall D3DXVec3TransformNormal(ptr ptr ptr) d3dx9_36.D3DXVec3TransformNormal
@ stdcall D3DXVec3TransformNormalArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec3TransformNormalArray
@ stdcall D3DXVec3Unproject(ptr ptr ptr ptr ptr ptr) d3dx9_36.D3DXVec3Unproject
@ stdcall D3DXVec3UnprojectArray(ptr long ptr long ptr ptr ptr ptr long) d3dx9_36.D3DXVec3UnprojectArray
@ stdcall D3DXVec4BaryCentric(ptr ptr ptr ptr float float) d3dx9_36.D3DXVec4BaryCentric
@ stdcall D3DXVec4CatmullRom(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXVec4CatmullRom
@ stdcall D3DXVec4Cross(ptr ptr ptr ptr) d3dx9_36.D3DXVec4Cross
@ stdcall D3DXVec4Hermite(ptr ptr ptr ptr ptr float) d3dx9_36.D3DXVec4Hermite
@ stdcall D3DXVec4Normalize(ptr ptr) d3dx9_36.D3DXVec4Normalize
@ stdcall D3DXVec4Transform(ptr ptr ptr) d3dx9_36.D3DXVec4Transform
@ stdcall D3DXVec4TransformArray(ptr long ptr long ptr long) d3dx9_36.D3DXVec4TransformArray
