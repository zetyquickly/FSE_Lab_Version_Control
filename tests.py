from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    key = 'c'
    val = 3
    st.add(key,val)
    if st.data['c'] != 3:
        return 1
    key = 'a'
    try:
        st.add(key,val)
    except Exception:
        return 0
    return 1

def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key1 = 'b'
    key2 = 'c'
    try:
        st.remove(key1)
    except Exception:
        return 0
    try:
        st.remove(key2)
    except Exception:
        return 0
    return 1
    
    

def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.set(key, 3)
    assert st.get(key) == 3
    key = 'c'
    val = st.set(key, 4)
    assert val is None

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
