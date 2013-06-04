def LinearLeastSquaresFit(x,y):
    """takes input arrays of x and y and returns slope and intercept with corresponding errors"""
    x_avg = (1/float(len(x)))*sum(x)
    x_sqr_avg = (1/float(len(x)))*sum(x**2)
    y_avg = (1/float(len(x)))*sum(y)
    xy_avg = (1/float(len(x)))*sum(x*y)
    slope = (xy_avg - x_avg*y_avg)/(x_sqr_avg - x_avg**2)
    intercept = (x_sqr_avg * y_avg - x_avg*xy_avg)/(x_sqr_avg - x_avg**2)
    delta_sqr_avg = (1/float(len(x)))*(sum((y-(slope*x+intercept))**2))
    slope_error = (1/(float(len(x)-2)))**(1/2.)*(delta_sqr_avg/(x_sqr_avg - x_avg**2))**(1/2.)
    intercept_error = (1/(float(len(x)-2)))**(1/2.)*((delta_sqr_avg*x_sqr_avg)/(x_sqr_avg - x_avg**2))**(1/2.)
    return slope,intercept,slope_error,intercept_error


def WeightedLinearLeastSquaresFit(x,y,w):
    """ takes input arrays of x,y, and w and returns slope,slope error,intercept, and intercept error"""
    """remember w is 1/(u^2) where u is the uncertainty"""
    w_sum = sum(w)
    wy_sum = sum(w*y)
    wx_sum = sum(w*x)
    wxy_sum = sum(w*x*y)
    w_x_sqr_sum = sum(w*(x**2))
    wx_sum_sqr = (sum(w*x))**2
    intercept_ = (w_x_sqr_sum*wy_sum - wx_sum*wxy_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr)
    slope_ = (w_sum*wxy_sum - wx_sum*wy_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr)
    slope_error_ = ((w_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr))**(1/2.)
    intercept_error_ = ((w_x_sqr_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr))**(1/2.)
    return slope_,slope_error_,intercept_,intercept_error_
