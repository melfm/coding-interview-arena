package data_types;

import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Stack;

/**
 * Implement an iterator that provides a flattening iterator over a
 * Collection<?>.
 * 
 * i.e. The constructor takes in a Collection<?> object which may nest
 * either a Collection<?> object or an object of type T.
 * Also, it is expected that the nested Collection<?> objects will not
 * reference their container Collection<?> objects as this will lead
 * to a loop. But they can nest other Collection<?> objects. The class
 * then iterates through elements in the given Collection<?> object,
 * returning the values in the leaves of the nested structure one-by-one
 * upon each call to next().
 *
 * Example: This deep iterator can be used to iterate over a vector that
 *          either contains a vector of integers, or just plain integers,
 *          or both. Lets assume that the Collection<?> passed has the
 *          following structure:
 *
 *                           [int_a, vector_1, int_d, vector_2, int_h]
 *                                     /                 \
 *                                    /                   \
 *                               [int_b, int_c]        [int_e, vector_3]
 *                                                                /
 *                                                               /
 *                                                         [int_f, int_g]
 *
 *          The iterator returns the leaves in order viz.: int_a, int_b,
 *          int_c, int_d, int_e, int_f, int_g, int_h.
**/

public class DeepIterator<T> implements Iterator<T> {
		
	private final Stack<Iterator<?>> datStack;
	private T nextItem;
	
	// Constructor
	public DeepIterator(Collection<?> collection) {
		datStack = new Stack<Iterator<?>>();
		try
		{
			datStack.push(collection.iterator());
		} 
		catch(Exception e) {
			throw new NullPointerException("Collection cannot be null.");
		}
	}

	@SuppressWarnings("unchecked")
	@Override
	public boolean hasNext() {
		if(nextItem != null) {
			return true;
		}
		while(!datStack.empty()) {
			
			Iterator<?> iter = datStack.peek();
			
			if(iter.hasNext()) {
				Object item = iter.next();

				if(item instanceof Collection<?>) {
					// Push on to the stack
					datStack.push(((Collection<?>) item).iterator());
				} 
				else{
					// return the value
					nextItem = (T) item;
					return true;	
				}
			}	 
			else {
				datStack.pop();
			}
			
		}
		return false;
	}

	@Override
	public T next() {
		if(hasNext()) {
			T returnMe = nextItem;
			System.out.println(nextItem);
			nextItem = null;
			return returnMe;
		}
		throw new NoSuchElementException();
	}

	@Override
	public void remove() {
		throw new UnsupportedOperationException();
		
	}	

}
