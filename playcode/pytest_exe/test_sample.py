import pytest
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def inc(s):
    return s+1

def test_ans():
    assert inc(3)==5
if __name__=='__main__':
    pytest.main()


