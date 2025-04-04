from fpdf import FPDF

def generate_renewable_energy_report():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    
    # Title
    pdf.cell(200, 10, "Renewable Energy Trends 2025", ln=True, align='C')
    pdf.ln(10)

    # Summary Points
    pdf.set_font("Arial", size=12)
    summary = [
        "- Solar energy adoption increased by 35% in the last 3 years",
        "- Wind power installations have doubled in Europe and Asia",
        "- Governments are investing heavily in hydro and geothermal energy",
        "- Key challenges: Storage, transmission, and cost"
    ]
    
    for line in summary:
        pdf.cell(0, 10, line, ln=True)

    pdf.ln(10)

    # Pie Chart - Renewable Energy Distribution
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, "Renewable Energy Distribution", ln=True, align='C')
    pdf.image("output/pie_chart.png", x=40, w=130)  # Adjust position and width

    pdf.ln(10)

    # Line Chart - Solar Energy Growth
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, "Solar Energy Growth Over the Years", ln=True, align='C')
    pdf.image("output/energy_chart.png", x=30, w=150)  # Adjust position and width

    # Save the report
    pdf.output("output/renewable_energy_report.pdf")
    print("✅ Report saved as 'output/renewable_energy_report.pdf'")

# Run the function
generate_renewable_energy_report()
