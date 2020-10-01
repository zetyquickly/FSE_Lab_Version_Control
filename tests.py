from storage import Storage

def test_add():
    st = Storage({})
    key, val = 'b', 3
    st.add(key, val)
    assert st.get(key) == val, "Value for the key {} is not equal to expected".format(key)

def test_remove():
    pass

def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    new_val = 3
    st.set(key,new_val)
    assert st.get(key) == new_val, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    new_val = 3
    st.set(key,new_val)
    assert st.get(key) is None, "Value for an unexisting key is not None"

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
