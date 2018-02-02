### Starter code for Homework 2, problem 7 ###

#Our true mean function: will be sin(x/2) on [0,4*pi] and sin(6*x) on [4*pi,8*pi]
mu = function(x){
  #Initialize a vector of zeros
  y = numeric(length(x))
  #Figure out which points are to the left or right of 4*pi
  left_points = (x<=4*pi)
  right_points = (x>4*pi)
  #Assign the appropriate sine values
  y[left_points] = sin(x[left_points]/2)
  y[right_points] = sin(6*x[right_points])
  #Return y
  y
}

#A function to draw a sample from this curve
generate_sample = function(n){
  #Sample the x coordinates uniformly on [0,8*pi].
  #We sort the x here to make plotting easier later.
  x = sort(runif(n,0,6*pi))
  #Sample the y coordinates as gaussians around mu(x)
  y = mu(x) + rnorm(n,0,.2)
  #Bind this all together into a data frame
  data.frame(x=x,y=y)  
}

#We set the seed so that your homeworks will match
set.seed(7)
#Sample 300 points.  This is your data set!
data = generate_sample(300)
