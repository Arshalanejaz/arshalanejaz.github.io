# import streamlit as st
# import gspread
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import base64
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import os

# # ============ IDfy BRANDING ============
# IDFY_RED = "#CE1010"
# IDFY_BLUE = "#1C43B9"

# # ============ PAGE CONFIG ============
# st.set_page_config(
#     page_title="IDfy Email Extractor",
#     layout="wide",
#     initial_sidebar_state="collapsed",
#     menu_items=None
# )

# # ============ CUSTOM CSS ============
# st.markdown(f"""
# <style>
# * {{
#     margin: 0;
#     padding: 0;
#     box-sizing: border-box;
# }}

# .landing-page {{
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     min-height: 100vh;
#     background: linear-gradient(135deg, {IDFY_RED} 0%, {IDFY_BLUE} 100%);
#     color: white;
#     text-align: center;
#     padding: 40px 20px;
# }}

# .landing-icon {{
#     font-size: 100px;
#     margin-bottom: 20px;
# }}

# .landing-title {{
#     font-size: 48px;
#     font-weight: bold;
#     margin-bottom: 10px;
# }}

# .landing-subtitle {{
#     font-size: 24px;
#     margin-bottom: 10px;
#     opacity: 0.95;
# }}

# .landing-tagline {{
#     font-size: 14px;
#     opacity: 0.85;
#     font-style: italic;
#     margin-bottom: 40px;
# }}

# .start-btn {{
#     background: white;
#     color: {IDFY_RED};
#     padding: 15px 50px;
#     font-size: 18px;
#     font-weight: bold;
#     border: none;
#     border-radius: 8px;
#     cursor: pointer;
#     transition: all 0.3s;
# }}

# .start-btn:hover {{
#     transform: translateY(-2px);
#     box-shadow: 0 8px 20px rgba(0,0,0,0.2);
# }}

# .main-header {{
#     background: linear-gradient(135deg, {IDFY_RED} 0%, {IDFY_BLUE} 100%);
#     padding: 25px;
#     border-radius: 12px;
#     color: white;
#     margin-bottom: 25px;
#     text-align: center;
#     box-shadow: 0 4px 15px rgba(0,0,0,0.1);
# }}

# .main-header h1 {{
#     font-size: 28px;
#     margin: 0;
#     font-weight: bold;
# }}

# .main-header p {{
#     font-size: 13px;
#     opacity: 0.9;
#     margin: 8px 0 0 0;
# }}

# .container {{
#     display: grid;
#     grid-template-columns: 1fr 300px;
#     gap: 20px;
# }}

# .form-section {{
#     background: white;
#     padding: 20px;
#     border-radius: 10px;
#     box-shadow: 0 2px 10px rgba(0,0,0,0.08);
# }}

# .section-title {{
#     font-size: 15px;
#     font-weight: bold;
#     color: {IDFY_RED};
#     margin-bottom: 15px;
#     padding-bottom: 10px;
#     border-bottom: 2px solid {IDFY_RED};
# }}

# .form-row {{
#     display: grid;
#     grid-template-columns: 1fr 1fr;
#     gap: 12px;
#     margin-bottom: 15px;
# }}

# .form-group {{
#     margin-bottom: 12px;
# }}

# .form-group label {{
#     display: block;
#     font-weight: bold;
#     font-size: 12px;
#     color: #333;
#     margin-bottom: 5px;
# }}

# .form-group input,
# .form-group select {{
#     width: 100%;
#     padding: 10px;
#     border: 1px solid #ddd;
#     border-radius: 6px;
#     font-size: 12px;
# }}

# .form-group input:focus,
# .form-group select:focus {{
#     outline: none;
#     border-color: {IDFY_RED};
#     box-shadow: 0 0 0 2px rgba(206, 16, 16, 0.1);
# }}

# .btn {{
#     width: 100%;
#     padding: 10px;
#     border: none;
#     border-radius: 6px;
#     font-size: 13px;
#     font-weight: bold;
#     cursor: pointer;
#     transition: all 0.2s;
#     margin-bottom: 8px;
# }}

# .btn:hover {{
#     transform: translateY(-1px);
#     box-shadow: 0 4px 12px rgba(0,0,0,0.15);
# }}

# .btn-primary {{
#     background: linear-gradient(135deg, {IDFY_RED} 0%, {IDFY_BLUE} 100%);
#     color: white;
# }}

# .btn-secondary {{
#     background: linear-gradient(135deg, {IDFY_BLUE} 0%, #4c63d2 100%);
#     color: white;
# }}

# .btn-success {{
#     background: linear-gradient(135deg, #10b981 0%, #059669 100%);
#     color: white;
# }}

# .timestamp-box {{
#     background: linear-gradient(135deg, #fef3c7 0%, #fff8dc 100%);
#     padding: 15px;
#     border-radius: 8px;
#     border: 2px solid #fbbf24;
#     margin: 15px 0;
# }}

# .timestamp-box label {{
#     color: #78350f;
#     font-weight: bold;
#     font-size: 12px;
# }}

# .timestamp-box input {{
#     background: white;
#     border-color: #fbbf24;
# }}

# .timestamp-hint {{
#     font-size: 10px;
#     color: #78350f;
#     margin-top: 5px;
#     font-style: italic;
# }}

# .email-panel {{
#     background: white;
#     padding: 15px;
#     border-radius: 10px;
#     box-shadow: 0 2px 10px rgba(0,0,0,0.08);
#     max-height: 700px;
#     overflow-y: auto;
# }}

# .email-header {{
#     font-weight: bold;
#     font-size: 13px;
#     color: {IDFY_RED};
#     margin-bottom: 10px;
#     padding-bottom: 8px;
#     border-bottom: 2px solid {IDFY_RED};
# }}

# .email-item {{
#     background: #f5f5f5;
#     padding: 8px;
#     border-radius: 5px;
#     font-size: 10px;
#     margin-bottom: 6px;
#     word-break: break-all;
#     border-left: 3px solid {IDFY_BLUE};
#     color: #333;
# }}

# .status {{
#     padding: 12px;
#     border-radius: 6px;
#     font-size: 12px;
#     margin-bottom: 12px;
#     border-left: 4px solid;
# }}

# .status.success {{
#     background: #d1fae5;
#     color: #065f46;
#     border-left-color: #10b981;
# }}

# .status.error {{
#     background: #fee2e2;
#     color: #991b1b;
#     border-left-color: #ef4444;
# }}

# .status.info {{
#     background: #dbeafe;
#     color: #1e40af;
#     border-left-color: #3b82f6;
# }}

# </style>
# """, unsafe_allow_html=True)

# # ============ GOOGLE AUTH ============
# @st.cache_resource
# def authenticate_sheets():
#     """Authenticate Google Sheets API"""
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
#     try:
#         if os.path.exists('credentials.json'):
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#             return build('sheets', 'v4', credentials=creds)
#     except Exception as e:
#         st.error(f"❌ Sheets auth error: {e}")
#         return None

# @st.cache_resource
# def authenticate_gmail():
#     """Authenticate Gmail API"""
#     SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
#     try:
#         if os.path.exists('credentials.json'):
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#             return build('gmail', 'v1', credentials=creds)
#     except Exception as e:
#         st.error(f"❌ Gmail auth error: {e}")
#         return None

# # ============ DATA FUNCTIONS ============
# def get_products_and_apis(spreadsheet_id):
#     """Fetch products and APIs from Google Sheet"""
#     try:
#         sheets_service = authenticate_sheets()
#         if not sheets_service:
#             return None, None
        
#         result = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
#         sheets = result.get('sheets', [])
        
#         products = [sheet['properties']['title'] for sheet in sheets]
#         products.sort()
        
#         apis = {}
#         for product in products:
#             try:
#                 range_name = f"'{product}'!D2:D1000"
#                 result = sheets_service.spreadsheets().values().get(
#                     spreadsheetId=spreadsheet_id,
#                     range=range_name
#                 ).execute()
                
#                 values = result.get('values', [])
#                 api_set = set()
#                 for row in values:
#                     if row and row[0]:
#                         api_set.add(row[0].strip())
                
#                 apis[product] = sorted(list(api_set))
#             except:
#                 apis[product] = []
        
#         return products, apis
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#         return None, None

# def extract_emails(spreadsheet_id, product, api):
#     """Extract emails for selected product and API"""
#     try:
#         sheets_service = authenticate_sheets()
#         if not sheets_service:
#             return []
        
#         SOURCE_API_COL = 4
#         SOURCE_EMAIL_COLS = [7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        
#         range_name = f"'{product}'!A2:Z1000"
#         result = sheets_service.spreadsheets().values().get(
#             spreadsheetId=spreadsheet_id,
#             range=range_name
#         ).execute()
        
#         rows = result.get('values', [])
#         matches = []
        
#         for row in rows:
#             if len(row) > SOURCE_API_COL - 1:
#                 api_val = row[SOURCE_API_COL - 1].strip() if row[SOURCE_API_COL - 1] else ""
#                 if api_val.lower() == api.lower():
#                     for col_idx in SOURCE_EMAIL_COLS:
#                         if len(row) > col_idx - 1 and row[col_idx - 1]:
#                             emails = row[col_idx - 1].split(';')
#                             for email in emails:
#                                 email = email.strip()
#                                 if email and '@' in email:
#                                     matches.append(email)
        
#         matches = list(set(matches))
#         return matches
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#         return []

# def create_html_body(api_name, timestamp=None):
#     """Create HTML email body"""
#     if timestamp and timestamp.strip():
#         html = f"""
#         <html>
#           <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
#             <p>Dear Valued Customer,</p>
#             <p>We hope this message finds you well.</p>
#             <p>We are writing to inform you about an ongoing issue affecting the <strong>{api_name} Verification API</strong>.</p>
#             <p style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 12px; margin: 15px 0;">
#               <strong>⏰ Downtime Started:</strong> {timestamp}
#             </p>
#             <p>The API is currently experiencing downtime due to technical difficulties on the source website.</p>
#             <p>While this situation is beyond our control, please be assured that we are dedicated to resolving this matter as swiftly as possible.</p>
#             <p>Thank you for your understanding and patience.</p>
#             <p>Regards,<br><strong>IDfy Support</strong></p>
#           </body>
#         </html>
#         """
#     else:
#         html = f"""
#         <html>
#           <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
#             <p>Dear Valued Customer,</p>
#             <p>We are writing to inform you about an ongoing issue affecting the <strong>{api_name} Verification API</strong>.</p>
#             <p>The API is currently experiencing downtime due to technical difficulties on the source website.</p>
#             <p>While this situation is beyond our control, we are dedicated to resolving this matter as swiftly as possible.</p>
#             <p>Thank you for your understanding and patience.</p>
#             <p>Regards,<br><strong>IDfy Support</strong></p>
#           </body>
#         </html>
#         """
#     return html

# def create_gmail_draft(from_email, to_emails, subject, html_body, bcc_email=None):
#     """Create Gmail draft"""
#     try:
#         gmail_service = authenticate_gmail()
#         if not gmail_service:
#             return False, "Gmail service not authenticated"
        
#         message = MIMEMultipart('alternative')
#         message['subject'] = subject
#         message['from'] = from_email
#         message['to'] = from_email
        
#         if bcc_email:
#             all_bcc = [bcc_email] + to_emails
#             message['bcc'] = ','.join(all_bcc)
        
#         part = MIMEText(html_body, 'html')
#         message.attach(part)
        
#         create_message = {
#             'message': {
#                 'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
#             }
#         }
        
#         draft = gmail_service.users().drafts().create(userId='me', body=create_message).execute()
#         draft_id = draft['id']
#         draft_url = f"https://mail.google.com/mail/u/0/#drafts?compose={draft_id}"
        
#         return True, draft_url
#     except Exception as e:
#         return False, str(e)

# # ============ PRODUCT MAPPING ============
# PRODUCT_CLIENT_EMAIL_MAP = {
#     "VS OU_SPOC_list": "vkyc.support@idfy.com",
#     "VS OU_SPOC_list_International": "vkyc.support@idfy.com",
#     "EVE/360_international": "360.support@idfy.com",
#     "EVE_OU Details": "eve.support@idfy.com"
# }

# PRODUCT_FRESHDESK_BCC_MAP = {
#     "VS OU_SPOC_list": "Help.support@idfy.com",
#     "VS OU_SPOC_list_International": "Help.support@idfy.com",
#     "EVE/360_international": "Help.support@idfy.com",
#     "EVE_OU Details": "360.support@idfy.com"
# }

# # ============ MAIN APP ============
# def main():
#     # Initialize session state
#     if 'app_started' not in st.session_state:
#         st.session_state.app_started = False
#     if 'emails_extracted' not in st.session_state:
#         st.session_state.emails_extracted = False
#     if 'extracted_emails' not in st.session_state:
#         st.session_state.extracted_emails = []
#     if 'sheet_id' not in st.session_state:
#         st.session_state.sheet_id = "1eHMvYF3lesJxLFPNwQaMjSd9yg9dhG58EF7Kj3fZnDc"
    
#     # === LANDING PAGE ===
#     if not st.session_state.app_started:
#         st.markdown("""
#         <div class="landing-page">
#             <div class="landing-icon">🛡️</div>
#             <div class="landing-title">IDfy</div>
#             <div class="landing-subtitle">Email Extractor</div>
#             <div class="landing-tagline">Integrated Identity Platform</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns(3)
#         with col2:
#             if st.button("🚀 START", use_container_width=True, key="start_btn"):
#                 st.session_state.app_started = True
#                 st.rerun()
    
#     # === MAIN APP ===
#     else:
#         # Header
#         st.markdown("""
#         <div class="main-header">
#             <h1>📧 Email Extractor Pro</h1>
#             <p>IDfy - Integrated Identity Platform</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Main content
#         col_form, col_emails = st.columns([1, 0.28])
        
#         with col_form:
#             # === STEP 1: SPREADSHEET ID & LOAD ===
#             st.markdown('<div class="form-section"><div class="section-title">📋 Step 1: Connect & Load</div>', unsafe_allow_html=True)
            
#             sheet_id = st.text_input(
#                 "🗂️ Source Spreadsheet ID",
#                 value=st.session_state.sheet_id,
#                 key="sheet_input"
#             )
#             st.session_state.sheet_id = sheet_id
            
#             load_col1, load_col2 = st.columns([2, 1])
#             with load_col2:
#                 if st.button("📥 Load", use_container_width=True, key="load_btn"):
#                     with st.spinner("⏳ Loading..."):
#                         products, apis = get_products_and_apis(sheet_id)
#                         if products:
#                             st.session_state.products = products
#                             st.session_state.apis = apis
#                             st.success("✅ Loaded!")
#                         else:
#                             st.error("❌ Failed to load")
            
#             st.markdown('</div>', unsafe_allow_html=True)
            
#             # === STEP 2: PRODUCT & API ===
#             if 'products' in st.session_state:
#                 st.markdown('<div class="form-section"><div class="section-title">⚙️ Step 2: Select Product & API</div>', unsafe_allow_html=True)
                
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     product = st.selectbox(
#                         "📦 Product",
#                         st.session_state.products,
#                         key="product_select"
#                     )
                
#                 with col2:
#                     apis_list = st.session_state.apis.get(product, [])
#                     api = st.selectbox(
#                         "⚙️ API",
#                         apis_list if apis_list else ["No APIs"],
#                         key="api_select"
#                     )
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # === STEP 3: EXTRACT ===
#                 st.markdown('<div class="form-section"><div class="section-title">📋 Step 3: Extract Emails</div>', unsafe_allow_html=True)
                
#                 if st.button("📋 Extract Emails", use_container_width=True, key="extract_btn"):
#                     with st.spinner("⏳ Extracting..."):
#                         emails = extract_emails(sheet_id, product, api)
#                         st.session_state.extracted_emails = emails
#                         st.session_state.emails_extracted = True
#                         st.session_state.selected_product = product
#                         st.session_state.selected_api = api
                    
#                     if emails:
#                         st.success(f"✅ Extracted {len(emails)} emails!")
#                     else:
#                         st.warning("⚠️ No emails found")
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # === STEP 4: INSIGHTS DASHBOARD ===
#                 st.markdown('<div class="form-section"><div class="section-title">📊 Tools</div>', unsafe_allow_html=True)
                
#                 if st.button("📊 Open Insights Dashboard", use_container_width=True):
#                     st.markdown("[Open Dashboard](https://insights.idfy.com/)")
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # === STEP 5: TIMESTAMP ===
#                 if st.session_state.emails_extracted:
#                     st.markdown("""
#                     <div class="timestamp-box">
#                     <label>⏰ Downtime Start Time (Optional)</label>
#                     <p class="timestamp-hint">Format: e.g., 01 Nov 2025, 02:30 PM</p>
#                     </div>
#                     """, unsafe_allow_html=True)
                    
#                     timestamp = st.text_input(
#                         "Enter timestamp",
#                         key="timestamp_input",
#                         placeholder="Leave blank for standard email"
#                     )
                    
#                     # === STEP 6: SEND EMAIL ===
#                     st.markdown('<div class="form-section"><div class="section-title">✉️ Step 6: Send Email</div>', unsafe_allow_html=True)
                    
#                     if st.button("✉️ Send Email", use_container_width=True, key="send_btn"):
#                         product = st.session_state.selected_product
#                         api = st.session_state.selected_api
                        
#                         from_email = PRODUCT_CLIENT_EMAIL_MAP.get(product)
#                         freshdesk_bcc = PRODUCT_FRESHDESK_BCC_MAP.get(product)
                        
#                         if not from_email:
#                             st.markdown('<div class="status error">❌ Product not configured</div>', unsafe_allow_html=True)
#                         else:
#                             subject = f"Important Notice: Intermittent Service Down - {api} Verification API"
#                             html_body = create_html_body(api, timestamp)
                            
#                             with st.spinner("⏳ Creating draft..."):
#                                 success, result = create_gmail_draft(
#                                     from_email,
#                                     st.session_state.extracted_emails,
#                                     subject,
#                                     html_body,
#                                     freshdesk_bcc
#                                 )
                            
#                             if success:
#                                 st.markdown(f"""
#                                 <div class="status success">
#                                 ✅ <strong>Draft Created!</strong><br>
#                                 📧 From: {from_email}<br>
#                                 🎫 BCC: {freshdesk_bcc}<br>
#                                 ⏰ Timestamp: {timestamp if timestamp else 'Not included'}<br>
#                                 <a href="{result}" target="_blank">→ Open in Gmail</a>
#                                 </div>
#                                 """, unsafe_allow_html=True)
#                             else:
#                                 st.markdown(f'<div class="status error">❌ {result}</div>', unsafe_allow_html=True)
                    
#                     st.markdown('</div>', unsafe_allow_html=True)
        
#         # === EMAIL PANEL (RIGHT SIDE) ===
#         with col_emails:
#             st.markdown('<div class="email-panel">', unsafe_allow_html=True)
#             st.markdown(f'<div class="email-header">📧 Extracted Emails ({len(st.session_state.extracted_emails)})</div>', unsafe_allow_html=True)
            
#             if st.session_state.extracted_emails:
#                 for idx, email in enumerate(st.session_state.extracted_emails[:50], 1):
#                     st.markdown(f'<div class="email-item">{idx}. {email}</div>', unsafe_allow_html=True)
                
#                 if len(st.session_state.extracted_emails) > 50:
#                     st.markdown(f'<div class="email-item" style="background: #e0e0e0; color: #666;">... +{len(st.session_state.extracted_emails) - 50} more</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown('<div style="padding: 10px; color: #999; font-size: 11px;">Click "Extract Emails" to populate list</div>', unsafe_allow_html=True)
            
#             st.markdown('</div>', unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()


import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="IDfy Email Extractor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CUSTOM CSS
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.landing-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #CE1010 0%, #1C43B9 100%);
    color: white;
    text-align: center;
    padding: 40px 20px;
}

.landing-icon {
    font-size: 100px;
    margin-bottom: 20px;
}

.landing-title {
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 10px;
}

.landing-subtitle {
    font-size: 24px;
    margin-bottom: 10px;
    opacity: 0.95;
}

.landing-tagline {
    font-size: 14px;
    opacity: 0.85;
    font-style: italic;
    margin-bottom: 40px;
}

.main-header {
    background: linear-gradient(135deg, #CE1010 0%, #1C43B9 100%);
    padding: 25px;
    border-radius: 12px;
    color: white;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.main-header h1 {
    font-size: 28px;
    margin: 0;
    font-weight: bold;
}

.main-header p {
    font-size: 13px;
    opacity: 0.9;
    margin: 8px 0 0 0;
}

.form-section {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.section-title {
    font-size: 15px;
    font-weight: bold;
    color: #CE1010;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid #CE1010;
}

.email-panel {
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    max-height: 700px;
    overflow-y: auto;
}

.email-header {
    font-weight: bold;
    font-size: 13px;
    color: #CE1010;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 2px solid #CE1010;
}

.email-item {
    background: #f5f5f5;
    padding: 8px;
    border-radius: 5px;
    font-size: 10px;
    margin-bottom: 6px;
    word-break: break-all;
    border-left: 3px solid #1C43B9;
    color: #333;
}

.status {
    padding: 12px;
    border-radius: 6px;
    font-size: 12px;
    margin-bottom: 12px;
    border-left: 4px solid;
}

.status.success {
    background: #d1fae5;
    color: #065f46;
    border-left-color: #10b981;
}

.timestamp-box {
    background: linear-gradient(135deg, #fef3c7 0%, #fff8dc 100%);
    padding: 15px;
    border-radius: 8px;
    border: 2px solid #fbbf24;
    margin: 15px 0;
}

.timestamp-box label {
    color: #78350f;
    font-weight: bold;
    font-size: 12px;
}

.timestamp-hint {
    font-size: 10px;
    color: #78350f;
    margin-top: 5px;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if 'app_started' not in st.session_state:
    st.session_state.app_started = False
if 'extracted_emails' not in st.session_state:
    st.session_state.extracted_emails = []
if 'emails_extracted' not in st.session_state:
    st.session_state.emails_extracted = False
if 'products' not in st.session_state:
    st.session_state.products = None
if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None

# DEMO DATA
DEMO_PRODUCTS = {
    "VS OU_SPOC_list": ["Product_2_API_1", "Product_2_API_2", "Product_2_API_3"],
    "VS OU_SPOC_list_International": ["API_International_1", "API_International_2"],
    "EVE/360_international": ["EVE_API_1", "EVE_API_2"],
    "EVE_OU Details": ["OU_API_1", "OU_API_2"]
}

DEMO_EMAILS = {
    "Product_2_API_1": [
        "john.doe@company.com",
        "jane.smith@company.com",
        "support@company.com",
        "admin@company.com",
        "contact@company.com"
    ],
    "Product_2_API_2": [
        "team@company.com",
        "info@company.com",
        "help@company.com",
        "sales@company.com",
        "marketing@company.com"
    ],
    "API_International_1": [
        "global@company.com",
        "international@company.com",
        "world@company.com"
    ]
}

PRODUCT_EMAIL_MAP = {
    "VS OU_SPOC_list": "vkyc.support@idfy.com",
    "VS OU_SPOC_list_International": "vkyc.support@idfy.com",
    "EVE/360_international": "360.support@idfy.com",
    "EVE_OU Details": "eve.support@idfy.com"
}

PRODUCT_BCC_MAP = {
    "VS OU_SPOC_list": "Help.support@idfy.com",
    "VS OU_SPOC_list_International": "Help.support@idfy.com",
    "EVE/360_international": "Help.support@idfy.com",
    "EVE_OU Details": "360.support@idfy.com"
}

# ===== LANDING PAGE =====
if not st.session_state.app_started:
    st.markdown("""
    <div class="landing-page">
        <div class="landing-icon">🛡️</div>
        <div class="landing-title">IDfy</div>
        <div class="landing-subtitle">Email Extractor</div>
        <div class="landing-tagline">Integrated Identity Platform</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🚀 START", use_container_width=True):
            st.session_state.app_started = True
            st.rerun()

# ===== MAIN APP =====
else:
    # HEADER
    st.markdown("""
    <div class="main-header">
        <h1>📧 Email Extractor Pro</h1>
        <p>IDfy - Integrated Identity Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # MAIN CONTENT
    col_form, col_emails = st.columns([1, 0.28])
    
    with col_form:
        # ===== STEP 1: CONNECT & LOAD =====
        st.markdown('<div class="form-section"><div class="section-title">📋 Step 1: Connect & Load</div>', unsafe_allow_html=True)
        
        sheet_id = st.text_input(
            "🗂️ Source Spreadsheet ID",
            value="1eHMvYF3lesJxLFPNwQaMjSd9yg9dhG58EF7Kj3fZnDc",
            disabled=True
        )
        
        col1, col2 = st.columns([2, 1])
        with col2:
            if st.button("📥 Load", use_container_width=True, key="load_btn"):
                st.session_state.products = list(DEMO_PRODUCTS.keys())
                st.success("✅ Loaded 4 products!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # ===== STEP 2: SELECT PRODUCT & API =====
        if st.session_state.products:
            st.markdown('<div class="form-section"><div class="section-title">⚙️ Step 2: Select Product & API</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                product = st.selectbox(
                    "📦 Product",
                    st.session_state.products,
                    key="product_select"
                )
                st.session_state.selected_product = product
            
            with col2:
                apis = DEMO_PRODUCTS.get(product, [])
                api = st.selectbox(
                    "⚙️ API",
                    apis,
                    key="api_select"
                )
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # ===== STEP 3: EXTRACT EMAILS =====
            st.markdown('<div class="form-section"><div class="section-title">📋 Step 3: Extract Emails</div>', unsafe_allow_html=True)
            
            if st.button("📋 Extract Emails", use_container_width=True, key="extract_btn"):
                emails = DEMO_EMAILS.get(api, DEMO_EMAILS.get("Product_2_API_1", []))
                st.session_state.extracted_emails = emails
                st.session_state.emails_extracted = True
                st.success(f"✅ Extracted {len(emails)} emails!")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # ===== STEP 4: TOOLS =====
            st.markdown('<div class="form-section"><div class="section-title">📊 Tools</div>', unsafe_allow_html=True)
            
            if st.button("📊 Open Insights Dashboard", use_container_width=True):
                st.info("📊 Opening Insights Dashboard... (Demo)")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # ===== STEP 5: TIMESTAMP =====
            if st.session_state.emails_extracted:
                st.markdown("""
                <div class="timestamp-box">
                <label>⏰ Downtime Start Time (Optional)</label>
                <p class="timestamp-hint">Format: e.g., 01 Nov 2025, 02:30 PM</p>
                </div>
                """, unsafe_allow_html=True)
                
                timestamp = st.text_input(
                    "Enter timestamp",
                    key="timestamp_input",
                    placeholder="Leave blank for standard email"
                )
                
                # ===== STEP 6: SEND EMAIL =====
                st.markdown('<div class="form-section"><div class="section-title">✉️ Step 6: Send Email</div>', unsafe_allow_html=True)
                
                if st.button("✉️ Send Email", use_container_width=True, key="send_btn"):
                    product = st.session_state.selected_product
                    from_email = PRODUCT_EMAIL_MAP.get(product, "support@idfy.com")
                    bcc_email = PRODUCT_BCC_MAP.get(product, "help@idfy.com")
                    
                    st.markdown(f"""
                    <div class="status success">
                    ✅ <strong>Draft Created Successfully!</strong><br>
                    📧 <strong>From:</strong> {from_email}<br>
                    🎫 <strong>BCC:</strong> {bcc_email}<br>
                    ⏰ <strong>Timestamp:</strong> {timestamp if timestamp else 'Not included'}<br>
                    📨 <strong>Recipients:</strong> {len(st.session_state.extracted_emails)} emails<br><br>
                    <a href="https://mail.google.com/mail/u/0/#drafts" target="_blank">→ Open in Gmail</a>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    # ===== EMAIL PANEL =====
    with col_emails:
        st.markdown('<div class="email-panel">', unsafe_allow_html=True)
        st.markdown(f'<div class="email-header">📧 Extracted Emails ({len(st.session_state.extracted_emails)})</div>', unsafe_allow_html=True)
        
        if st.session_state.extracted_emails:
            for idx, email in enumerate(st.session_state.extracted_emails, 1):
                st.markdown(f'<div class="email-item">{idx}. {email}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="padding: 10px; color: #999; font-size: 11px; text-align: center;">Click "Extract Emails" to populate</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
