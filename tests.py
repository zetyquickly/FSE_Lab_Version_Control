from storage import Storage

def test_add():
    pass

def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.remove(key)
    val = st.get(key)
    assert val is None, "Key {} is not deleted".format(key)
    key = 'c'
    try:
        st.remove(key)
    except KeyError as e:
        pass
    else:
        raise AssertionError("KeyError exception is not raised")

def test_set():
    pass

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