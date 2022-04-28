import app

def test_home_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """

    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data 

def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/mike' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data


def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/add_friend' route is requested (GET)
    THEN check that the user is redirected to the home page
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Estimator" in res.data
