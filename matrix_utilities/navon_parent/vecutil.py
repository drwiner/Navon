from vec import Vec

def list2vec(L):
    """Given a list L of field elements, return a Vec with domain {0...len(L)-1}
    whose entry i is L[i]

    >>> list2vec([10, 20, 30])
    Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
    """
    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})

def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})

def dilate(v, center, scale_factor):
    "returns a vector after dilating vector v from center at scale factor"
    displacement = v - center
    new_v = center + scale_factor*displacement;
    return new_v
	
def getDomainLength(v):
	return len(list(v.D))
    
def vecToTuple(v):
    point = [v[d] for d in v.f]
    return tuple(point);