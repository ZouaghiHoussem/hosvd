import numpy as np
if __name__ == "__main__":
	movieRatings = np.array(
	[
	[5,3,5],
	[4,2,1],
	[0,3,3],
	]
	, dtype='float64')

	# v1 = svd_1d(movieRatings)
	# print(v1)

	o_u, o_s, o_v = np.linalg.svd(movieRatings)
	print "input:\n", movieRatings, "\n"
	print "S:\n", o_s, "\nU:\n", o_u, "\nV:\n", o_v
