from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    new_key = 'c'
    new_value = 3
    st.add(new_key, new_value)
    assert ('c' in st.data) and (st.data['c'] == 3)
    try:
        st.add(new_key, new_value)
        assert False # make sure exception raises
    except Exception as e:
        pass

def test_remove():
    pass

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
