import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_epip_lines(img0, img1, lines, pts0, pts1, fast_viz=True):
    ''' img0 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r,c,_ = img0.shape
    if not fast_viz:
        img0 = cv2.cvtColor(img0,cv2.COLOR_BGR2RGB)
        img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        #TODO: implement visualization in matplotlib
    for r,pt0,pt1 in zip(lines,pts0,pts1):
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        img0 = cv2.line(img0, (x0,y0), (x1,y1), color,1)
        img0 = cv2.circle(img0,tuple(pt0.astype(int)),5,color,-1)
        img1 = cv2.circle(img1,tuple(pt1.astype(int)),5,color,-1)
        # img0 = cv2.drawMarker(img0,tuple(pt0.astype(int)),color,cv2.MARKER_CROSS,3)
        # img1 = cv2.drawMarker(img1,tuple(pt1.astype(int)),color,cv2.MARKER_CROSS,3)        
    return img0,img1


def make_matching_plot(image0, image1, pts0, pts1, pts_col=(0,0,255), point_size=2, line_col=(0,255,0), line_thickness=1, path=None, margin=10):
    if image0.ndim > 2:
        image0 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
    if image1.ndim > 2:
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)    
    H0, W0 = image0.shape
    H1, W1 = image1.shape
    H, W = max(H0, H1), W0 + W1 + margin

    out = 255*np.ones((H, W), np.uint8)
    out[:H0, :W0] = image0
    out[:H1, W0+margin:] = image1
    out = np.stack([out]*3, -1)

    mkpts0, mkpts1 = np.round(pts0).astype(int), np.round(pts1).astype(int)
    for (x0, y0), (x1, y1) in zip(mkpts0, mkpts1):
        cv2.line(out, (x0, y0), (x1 + margin + W0, y1),
                 color=line_col, thickness=line_thickness, lineType=cv2.LINE_AA)
        # display line end-points as circles
        cv2.circle(out, (x0, y0), point_size, pts_col, -1, lineType=cv2.LINE_AA)
        cv2.circle(out, (x1 + margin + W0, y1), point_size, pts_col, -1,
                   lineType=cv2.LINE_AA)
    if path is not None: 
        cv2.imwrite(path, out)
        
# Darw features
# img0 = images[1][0]
# pt0 = features[1][epoch].get_keypoints()
# # pts_col = tuple(np.random.randint(0,255,3).tolist())
# pts_col=(0,255,0)
# point_size=2
# # img0_features = cv2.drawMarker(img0,tuple(pt0.astype(int)),color,cv2.MARKER_CROSS,3)
# for (x0, y0) in pt0.astype(int):
    
    
    

# # Plot with OpenCV
# cam = 0
# i = 0
# xy = targets.get_im_coord(cam)[i]
# img = images[cam][i]
# cv2.namedWindow(f'cam {cam}, epoch {i}', cv2.WINDOW_NORMAL)
# color=(0,255,0)
# point_size=2
# img_target = cv2.drawMarker(img,tuple(xy.astype(int)),color,cv2.MARKER_CROSS,1)
# cv2.imshow(f'cam {cam}, epoch {i}', img_target) 
# cv2.waitKey()
# cv2.destroyAllWindows()

# #  Plot with matplotlib
# cam = 1
# i = 0
# _plot_style = dict(markersize=5, markeredgewidth=2,
#                    markerfacecolor='none', markeredgecolor='r',
#                    marker='x', linestyle='none')
# xy = targets.get_im_coord(cam)[i]
# img = cv2.cvtColor(images[cam][i], cv2.COLOR_BGR2RGB)
# fig, ax = plt.subplots()
# ax.imshow(img) 
# ax.plot(xy[0], xy[1], **_plot_style)
    

# x = np.arange(-10,10)
# y = x**2

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(x,y)

# coords = []

# def onclick(event):
#     global ix, iy
#     ix, iy = event.xdata, event.ydata
#     print(f'x = {ix}, y = {iy}')

#     global coords
#     coords.append((ix, iy))

#     if len(coords) == 2:
#         fig.canvas.mpl_disconnect(cid)

#     return coords
# cid = fig.canvas.mpl_connect('button_press_event', onclick)

    