import React, { useState } from 'react';

function Contact(){
    const [form, setForm] = useState({ name: '', email: '', subject: '', message: '' });
    const [submittedMessage, setSubmittedMessage] = useState(null);

    function handleChange(e){
        const { name, value } = e.target;
        setForm(f => ({ ...f, [name]: value }));
    }

    function handleSubmit(e){
        e.preventDefault();
        // For SmartHR this would be replaced with real submit logic
        setSubmittedMessage({ ...form, time: new Date().toLocaleString() });
        setForm({ name: '', email: '', subject: '', message: '' });
    }

    return (
        <div className="contact-page" style={{ maxWidth: 800, margin: '24px auto', padding: 16 }}>
            <h2>Contact SmartHR</h2>
            <p>If you have questions or feedback, please use the form below.</p>

            <form onSubmit={handleSubmit} style={{ display: 'grid', gap: 12 }}>
                <label>
                    Name
                    <input name="name" value={form.name} onChange={handleChange} required />
                </label>

                <label>
                    Email
                    <input name="email" type="email" value={form.email} onChange={handleChange} required />
                </label>

                <label>
                    Subject
                    <input name="subject" value={form.subject} onChange={handleChange} />
                </label>

                <label>
                    Message
                    <textarea name="message" value={form.message} onChange={handleChange} rows={6} required />
                </label>

                <div>
                    <button type="submit">Send Message</button>
                </div>
            </form>

            {submittedMessage && (
                <div style={{ marginTop: 24, padding: 12, border: '1px solid #ddd', borderRadius: 6 }}>
                    <h3>Submitted Message</h3>
                    <div><strong>Time:</strong> {submittedMessage.time}</div>
                    <div><strong>Name:</strong> {submittedMessage.name}</div>
                    <div><strong>Email:</strong> {submittedMessage.email}</div>
                    <div><strong>Subject:</strong> {submittedMessage.subject}</div>
                    <div style={{ marginTop: 8, whiteSpace: 'pre-wrap' }}><strong>Message:</strong>
                        <div style={{ marginTop: 6 }}>{submittedMessage.message}</div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default Contact;