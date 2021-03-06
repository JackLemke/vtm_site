def test_index_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested 
    THEN check that the output is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data

def test_about_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested 
    THEN check that the output is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the output is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance Estimator" in res.data

def test_estimate_vtm_calculation(app, client):
    '''
    GIVEN a user enters the radius and the height
    WHEN the the estimate amount is calulated
    THEN the final cost is estimated
    '''
    with app.test_client() as test_client:
        estimate = {"radius":"180", "height":"360"}
        res = test_client.post("/estimate", data=estimate)
        assert res.status_code == 200 
        assert b"$254,340.00." in res.data 

