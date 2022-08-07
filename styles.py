passport_style = f"""<style>
    @page {{
        size: A4 portrait;
        margin: 2cm;
    }}
    h1 {{
        margin: 0 auto 1cm;
        text-align: center;
        font-family: Roboto, Helvetica, Arial, Calbri, 'Liberation Serif';
        font-weight: 700;
        font-size: 20px;
    }}
    table {{
        border-collapse: collapse;
        border: 1px solid;
        font-family: Roboto, Helvetica, Arial, Calbri, 'Liberation Serif';
        font-weight: 400;
        font-size: 16px;
    }}
    th, td {{
        border: 1px solid;
        text-align: left;
        padding: 2mm;
        min-height: 8mm;
    }}
    .routes_list {{
        page-break-before: always;
    }}
    .signature {{
        display: flex;
        flex-direction: row;
    }}
</style>"""