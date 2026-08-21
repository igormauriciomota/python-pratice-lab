from app import create_app


app = create_app()


if __name__ == "__main__":
    # debug deve permanecer desativado na hospedagem.
    app.run(debug=True)
