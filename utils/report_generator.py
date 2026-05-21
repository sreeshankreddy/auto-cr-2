from fpdf import FPDF

class ReportGenerator:
    def generate_pdf(self, review_results, output_path):
        """
        Generates a PDF report based on review results.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Code Review Report", ln=True, align='C')
        pdf.ln(10)
        
        for key, value in review_results.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
            
        pdf.output(output_path)
        return output_path
