import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from fpdf import FPDF

# Load the CSV file
CSV_FILE_PATH = 'user_behavior_dataset.csv'
df = pd.read_csv(CSV_FILE_PATH)

# Generate basic statistics
def generate_statistics(df):
    stats_df = df.describe()
    return stats_df

# Visualization functions
def plot_histogram(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    df.hist(bins=20, ax=ax)
    plt.tight_layout()
    return fig

def plot_boxplot(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, ax=ax)
    plt.tight_layout()
    return fig

def plot_heatmap(df):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    return fig

# Generate PDF report
def generate_pdf_report(df, stats_df, hist_fig_path, box_fig_path, heatmap_fig_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Set font
    pdf.set_font("Arial", size=10)

    # Title
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align="C")

    # Basic Stats Section
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Statistical Summary:", ln=True)
    
    # Generate a shorter stats summary to fit within the page width
    stats_text = stats_df.to_string()
    pdf.multi_cell(180, 10, stats_text)  # Reduced width to fit the page

    # Add space before plots
    pdf.ln(10)

    # Histograms
    pdf.cell(200, 10, txt="Histograms", ln=True)
    pdf.image(hist_fig_path, x=10, w=180)  # Adjust width if necessary

    pdf.add_page()  # Start a new page for the next figures if needed

    # Box Plot
    pdf.cell(200, 10, txt="Box Plot", ln=True)
    pdf.image(box_fig_path, x=10, w=180)  # Adjust width if necessary

    # Add heatmap on a new page if necessary
    pdf.add_page()
    pdf.cell(200, 10, txt="Heatmap", ln=True)
    pdf.image(heatmap_fig_path, x=10, w=180)  # Adjust width if necessary

    # Save PDF to a buffer
    pdf_buffer = bytes(pdf.output(dest="S"))
    
    return pdf_buffer

# Main function
def main():
    st.title("Data Analysis and Report Generation")

    # Generate statistics
    stats_df = generate_statistics(df)
    
    # Generate plots
    hist_fig = plot_histogram(df)
    box_fig = plot_boxplot(df)
    heatmap_fig = plot_heatmap(df)
    
    # Save plots as images
    hist_fig_path = "histogram.png"
    box_fig_path = "boxplot.png"
    heatmap_fig_path = "heatmap.png"
    
    hist_fig.savefig(hist_fig_path)
    box_fig.savefig(box_fig_path)
    heatmap_fig.savefig(heatmap_fig_path)
    
    # Display statistics in Streamlit
    st.subheader("Statistical Summary")
    st.write(stats_df)

    # Display plots in Streamlit
    st.subheader("Histogram")
    st.pyplot(hist_fig)
    
    st.subheader("Box Plot")
    st.pyplot(box_fig)
    
    st.subheader("Heatmap")
    st.pyplot(heatmap_fig)
    
    # Generate PDF report
    pdf_buffer = generate_pdf_report(df, stats_df, hist_fig_path, box_fig_path, heatmap_fig_path)
    
    # Provide download link
    st.download_button("Download Report as PDF", data=pdf_buffer, file_name="data_analysis_report.pdf")

if __name__ == "__main__":
    main()
