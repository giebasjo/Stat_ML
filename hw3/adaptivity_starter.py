import scipy.stats

### Starter code for Homework 2, problem 7 ###

#Our true mean function: will be sin(x/2) on [0,4*pi] and sin(6*x) on [4*pi,8*pi]
def mu(x):
  #Initialize a vector of zeros
  y = np.zeros(len(x))
  #Figure out which points are to the left or right of 4*pi
  left_points = (x<=4*np.pi)
  right_points = (x>4*np.pi)
  #Assign the appropriate sine values
  y[left_points] = np.sin(x[left_points]/2.0)
  y[right_points] = np.sin(6*x[right_points])
  #Return y
  return(y)


#A function to draw a sample from this curve
def generate_sample(n):
  #Sample the x coordinates uniformly on [0,8*pi].
  #We sort the x here to make plotting easier later.
  x = np.random.uniform(low=0, high=8*np.pi, size=n)
  x.sort()

  #Sample the y coordinates as gaussians around mu(x)
  y = mu(x) + np.random.normal(loc=0, scale=0.2, size=n)
  #Bind this all together into a pandas data frame
  return(pd.DataFrame({'x':x, 'y':y}))
  #you can access like df['x'], df['y'], among many other ways


#We set the seed so that your homeworks will match
scipy.random.seed(7)
#Sample 300 points.  This is your data set!
data = generate_sample(500)
