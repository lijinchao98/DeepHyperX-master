import utils
import torch
import numpy as np
import sys
from log import Logger
# sys.stdout = Logger()
#
# HSI_image = utils.open_file(r'C:\Users\zheyong\Desktop\2.hdr')
# all_curve = HSI_image.read_pixel(0, 0)
# for raw in range(100):
#     for col in range(100):
#         pixel_curve = HSI_image.read_pixel(raw, col)
#         all_curve = np.vstack((all_curve, pixel_curve))
# all_curve = np.delete(all_curve, 0, 0)
# print(all_curve[0])
# print('*'*10)
# print(all_curve[9999])
# np.save('all_curve.npy', all_curve)
b = np.load('all_curve.npy')
b = b/10
np.save('all_curve.npy', b)
# print(b.shape)
# print(b[0])
# c = torch.tensor(b)
# print(c.size())
# print(c[0,:])
# print(len(c))
# w = np.array([])
# a = np.array([1,2,3])
# b = np.array([1,6,7])
# c = np.array([2,5,8])
#
# a = np.vstack((a, b))
# a = np.vstack((a, c))
# print(a)





import matplotlib.pyplot as plt
#
# l = [0.0093, 0.3037, 0.3847, 0.4897, 0.5879, 0.7342, 0.8338, 0.9158, 0.9896,
#         0.9910, 0.9795, 0.9715, 0.9577, 0.9492, 0.9406, 0.9285, 0.9161, 0.9025,
#         0.8889, 0.8761, 0.8622, 0.8474, 0.8347, 0.8221, 0.8111, 0.8027, 0.7957,
#         0.7912, 0.7896, 0.7887, 0.7880, 0.7882, 0.7875, 0.7877, 0.7873, 0.7853,
#         0.7817, 0.7772, 0.7745, 0.7733, 0.7749, 0.7782, 0.7817, 0.7860, 0.7897,
#         0.7928, 0.7958, 0.7982, 0.7997, 0.8011, 0.7997, 0.7964, 0.7913, 0.7837,
#         0.7768, 0.7693, 0.7614, 0.7534, 0.7431, 0.7317, 0.7200, 0.7072, 0.6960,
#         0.6854, 0.6753, 0.6664, 0.6570, 0.6478, 0.6395, 0.6314, 0.6250, 0.6201,
#         0.6170, 0.6160, 0.6146, 0.6133, 0.6101, 0.6053, 0.6002, 0.5939, 0.5875,
#         0.5810, 0.5758, 0.5710, 0.5674, 0.5642, 0.5602, 0.5567, 0.5532, 0.5501,
#         0.5462, 0.5414, 0.5339, 0.5241, 0.5122, 0.4960, 0.4755, 0.4506, 0.4231,
#         0.3954, 0.3683, 0.3426, 0.3187, 0.2984, 0.2863, 0.2804, 0.2819, 0.2882,
#         0.2976, 0.3107, 0.3239, 0.3393, 0.3532, 0.3668, 0.3790, 0.3889, 0.3952,
#         0.3986, 0.3979, 0.3928, 0.3845, 0.3719, 0.3591, 0.3468, 0.3361, 0.3276,
#         0.3218, 0.3172, 0.3163, 0.3179, 0.3208, 0.3286, 0.3390, 0.3535, 0.3701,
#         0.3822, 0.3847, 0.3808, 0.3695, 0.3555, 0.3435, 0.3303, 0.3278, 0.3352,
#         0.3614, 0.4087, 0.4394, 0.4432, 0.4300, 0.4153, 0.4017, 0.3774, 0.3874,
#         0.4405, 0.4986, 0.5646, 0.6268, 0.6724, 0.7294, 0.7779, 0.7905, 0.7801,
#         0.7148, 0.6536, 0.6174, 0.5768, 0.5533, 0.5095, 0.5221, 0.6028, 0.6726,
#         0.7241, 0.7773, 0.8762, 0.8776, 0.6445]
#
# q = [0.0309, 0.0308, 0.0310, 0.0328, 0.0339, 0.0350, 0.0348, 0.0369, 0.0363,
#         0.0366, 0.0375, 0.0382, 0.0385, 0.0377, 0.0368, 0.0367, 0.0369, 0.0361,
#         0.0363, 0.0358, 0.0356, 0.0349, 0.0348, 0.0342, 0.0341, 0.0340, 0.0339,
#         0.0335, 0.0332, 0.0330, 0.0335, 0.0334, 0.0331, 0.0331, 0.0327, 0.0326,
#         0.0327, 0.0327, 0.0326, 0.0331, 0.0325, 0.0325, 0.0328, 0.0324, 0.0327,
#         0.0323, 0.0321, 0.0322, 0.0323, 0.0319, 0.0318, 0.0317, 0.0312, 0.0313,
#         0.0310, 0.0306, 0.0304, 0.0302, 0.0295, 0.0292, 0.0290, 0.0286, 0.0284,
#         0.0281, 0.0277, 0.0275, 0.0274, 0.0271, 0.0274, 0.0274, 0.0268, 0.0265,
#         0.0262, 0.0258, 0.0256, 0.0254, 0.0249, 0.0245, 0.0242, 0.0237, 0.0239,
#         0.0240, 0.0237, 0.0233, 0.0229, 0.0230, 0.0231, 0.0227, 0.0220, 0.0216,
#         0.0211, 0.0202, 0.0196, 0.0194, 0.0191, 0.0178, 0.0173, 0.0165, 0.0159,
#         0.0151, 0.0144, 0.0144, 0.0143, 0.0139, 0.0148, 0.0150, 0.0145, 0.0149,
#         0.0149, 0.0154, 0.0160, 0.0152, 0.0149, 0.0152, 0.0142, 0.0139, 0.0139,
#         0.0139, 0.0137, 0.0132, 0.0125, 0.0131, 0.0132, 0.0124, 0.0121, 0.0114,
#         0.0113, 0.0106, 0.0106, 0.0103, 0.0105, 0.0112, 0.0110, 0.0116, 0.0119,
#         0.0124, 0.0128, 0.0125, 0.0142, 0.0144, 0.0150, 0.0141, 0.0139, 0.0143,
#         0.0135, 0.0128, 0.0120, 0.0114, 0.0085, 0.0082, 0.0064, 0.0050, 0.0043,
#         0.0058, 0.0050, 0.0065, 0.0099, 0.0100, 0.0100, 0.0099, 0.0099, 0.0115,
#         0.0116, 0.0153, 0.0153, 0.0138, 0.0096, 0.0096, 0.0096, 0.0089, 0.0090,
#         0.0126, 0.0140, 0.0065, 0.0075, 0.0088]
#
# x = range(len(q))
# y = q
# plt.plot(x, y, label='train loss', linewidth=2, color='r', marker='o', markerfacecolor='r', markersize=5)
# plt.xlabel('Epoch')
# plt.ylabel('Loss Value')
# plt.legend()
# plt.show()
#
#
