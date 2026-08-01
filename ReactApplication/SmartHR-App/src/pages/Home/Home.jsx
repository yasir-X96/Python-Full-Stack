import React from 'react';

const styles = {
  page: {
    padding: 32,
    fontFamily: 'Segoe UI, Roboto, sans-serif',
    color: '#1f2937',
    backgroundColor: '#f8fafc',
    minHeight: '100vh',
  },
  container: {
    maxWidth: '100%',
    margin: 0,
    backgroundColor: 'transparent',
    borderRadius: 0,
    boxShadow: 'none',
    padding: 0,
  },
  section: {
    marginTop: 28,
  },
  heading: {
    fontSize: 28,
    marginBottom: 12,
    color: '#111827',
  },
  text: {
    lineHeight: 1.75,
    fontSize: 16,
    color: '#4b5563',
  },
  grid: {
    display: 'grid',
    gap: 16,
    gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
    marginTop: 16,
  },
  list: {
    marginTop: 12,
    paddingLeft: 20,
    color: '#4b5563',
  },
  footer: {
    marginTop: 32,
    color: '#6b7280',
    textAlign: 'center',
    fontSize: 14,
  },
};

const Home = () => {
  return (
    <main style={styles.page}>
      <div style={styles.container}>
        <section style={styles.section}>
          <h1 style={styles.heading}>Welcome to SmartHR</h1>
          <p style={styles.text}>
            SmartHR helps small and medium teams manage employee information, time off, and HR
            workflows in a modern, easy-to-use interface. Built with React, this page demonstrates
            a clean, responsive layout and a polished onboarding experience.
          </p>
          <p style={styles.text}>
            Streamline hiring, onboarding, performance tracking, and compliance with a single
            solution designed to keep your team connected and your data organized.
          </p>
        </section>

        <section style={styles.section}>
          <h2 style={styles.heading}>Key Features</h2>
          <div style={styles.grid}>
            <div>
              <strong>Employee Directory</strong>
              <p style={styles.text}>Organize profiles, contact details, and roles in one place.</p>
            </div>
            <div>
              <strong>Time Off Management</strong>
              <p style={styles.text}>Send requests, approve leave, and track team availability.</p>
            </div>
            <div>
              <strong>Permissions & Roles</strong>
              <p style={styles.text}>Delegate access based on user roles and company policies.</p>
            </div>
            <div>
              <strong>Reporting</strong>
              <p style={styles.text}>Review activity logs, leave balances, and basic HR insights.</p>
            </div>
          </div>
        </section>

        <section style={styles.section}>
          <h2 style={styles.heading}>Getting Started</h2>
          <ol style={styles.list}>
            <li>Sign up or sign in to your SmartHR account.</li>
            <li>Invite team members and assign roles.</li>
            <li>Configure company settings and approval workflows.</li>
            <li>Start managing employees, leave, and reports.</li>
          </ol>
        </section>

        <section style={styles.section}>
          <h2 style={styles.heading}>Need Help?</h2>
          <p style={styles.text}>
            If you have questions or want to report an issue, contact your administrator or open an issue
            in the project repository.
          </p>
          <p style={styles.text}>
            For technical support, review the documentation, check the FAQ, or connect with your HR team for
            a guided setup.
          </p>
        </section>

        <section style={styles.section}>
          <h2 style={styles.heading}>Why Teams Choose SmartHR</h2>
          <p style={styles.text}>
            SmartHR was designed for teams that want a dependable HR platform without unnecessary complexity.
            It helps keep employee records accurate, approvals fast, and daily workflows organized.
          </p>
          <ul style={styles.list}>
            <li>Simple setup with step-by-step guidance.</li>
            <li>Secure data handling for employee privacy.</li>
            <li>Flexible workflows for managers and staff.</li>
          </ul>
        </section>

       
      </div>
    </main>
  );
};

export default Home;

