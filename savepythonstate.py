import dill #pip install dill --user

filename= 'globalsave.pkl'

dill.dump_session(filename)



def reloadstate( filename= 'globalsave.pkl' ):
    import dill #pip install dill --user

    filename= 'globalsave.pkl'

    return dill.load_session(filename)


'''
>>> # and if you get a pickling error, use dill's tools to discover a workaround
>>> dill.detect.badobjects(your_bad_object, depth=1)
>>>
>>> # visualize the references in your bad objects
>>> objgraph.show_refs(your_bad_object, filename='pygame_bad_object.png')
'''
