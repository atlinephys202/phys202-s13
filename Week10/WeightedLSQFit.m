function [slope_,slope_error_,intercept_,intercept_error_] = WeightedLSQFit(x,y,w)
% Takes input arrays of x,y, and w and returns slope,slope error,
% intercept, and intercept error.
% remember w is 1/(u^2) where u is the uncertainty
w_sum = sum(w);
wy_sum = sum(w.*y);
wx_sum = sum(w.*x);
wxy_sum = sum(w.*x.*y);
w_x_sqr_sum = sum(w.*(x.^2));
wx_sum_sqr = (sum(w.*x)).^2;
intercept_ = (w_x_sqr_sum*wy_sum - wx_sum*wxy_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr);
slope_ = (w_sum*wxy_sum - wx_sum*wy_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr);
slope_error_ = ((w_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr)).^(1/2.);
intercept_error_ = ((w_x_sqr_sum)/(w_sum*w_x_sqr_sum - wx_sum_sqr)).^(1/2.);

end

