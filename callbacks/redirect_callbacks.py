from dash import Output, Input, no_update


def add_redirect_callbacks(app):
    url_out = Output('url', 'pathname', allow_duplicate=True)

    @app.callback(url_out,
                  [Input("imdb-button", "n_clicks")],
                  prevent_initial_call=True)
    def logo_redirect(n_clicks):
        if n_clicks is not None:
            return "/main"

    @app.callback(url_out,
                  [Input("confirm-logout", "submit_n_clicks")],
                  prevent_initial_call=True)
    def logout_redirect(submit_n_clicks):
        if submit_n_clicks is not None:
            from flask import session
            session.pop('logged_in_user', None)
            # Redirect to the front page after logout
            return '/login'

    @app.callback(url_out,
                  [Input('redirect-to-main', 'n_intervals')],
                  prevent_initial_call=True)
    def redirect_to_main(n_intervals):
        if n_intervals > 0:
            return '/main'
        else:
            return no_update

    @app.callback(url_out,
                  [Input('movies-button', 'n_clicks')],
                  prevent_initial_call=True)
    def redirect_movies(n_clicks):
        if n_clicks is not None:
            return '/movies'

    @app.callback(url_out,
                  [Input('series-button', 'n_clicks')],
                  prevent_initial_call=True)
    def redirect_series(n_clicks):
        if n_clicks is not None:
            return '/series'

    @app.callback(url_out,
                  [Input('actors-button', 'n_clicks')],
                  prevent_initial_call=True)
    def redirect_actors(n_clicks):
        if n_clicks is not None:
            return '/actors'
