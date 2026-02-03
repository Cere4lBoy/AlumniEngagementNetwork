from flask import Blueprint, render_template, request, redirect, url_for

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# 1. DASHBOARD
@admin_bp.route('/admin/dashboard')
def dashboard():
    return render_template('admin/admin.html')

# 2. USER APPROVAL (Item 48)
@admin_bp.route('/users/approve')
def approve_users():
    # Make sure 'admin/user_approval.html' exists!
    return render_template('admin/user_approval.html')

# 3. SUSPEND USERS (Item 49)
@admin_bp.route('/users/suspend')
def suspend_users():
    return render_template('admin/suspend_user.html')

# 4. ASSIGN ROLES (Item 50)
@admin_bp.route('/users/roles')
def assign_roles():
    return render_template('admin/assign_roles.html')

# 5. RESET PASSWORD (Item 51)
@admin_bp.route('/users/reset-password')
def admin_reset_password():
    return render_template('admin/reset_user_password.html')

# 6. MANAGE EVENTS (Item 52/53 - The Main Event List)
@admin_bp.route('/events/manage')
def manage_events():
    return render_template('admin/event_management.html')

# 7. ANNOUNCEMENTS (Item 55)
@admin_bp.route('/events/announce')
def publish_announcement():
    return render_template('admin/publish_announcement.html')

# 8. MODERATION (Item 56/57)
@admin_bp.route('/testimonials')
def manage_testimonials():
    # Make sure 'admin/testimonial_approval.html' exists!
    return render_template('admin/testimonial_approval.html')

# 9. NOTIFICATIONS (Item 58)
@admin_bp.route('/system/notify')
def system_notification():
    return render_template('admin/send_notification.html')

# 10. SETTINGS (Item 59)
@admin_bp.route('/system/settings')
def system_settings():
    return render_template('admin/system_settings.html')

# --- HELPER ROUTES FOR BUTTON ACTIONS ---
# These are needed for the Create/Edit/Delete buttons inside the pages
@admin_bp.route('/events/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        return redirect(url_for('admin.manage_events'))
    return render_template('admin/event_create.html')

@admin_bp.route('/events/edit', methods=['GET', 'POST'])
def edit_event():
    if request.method == 'POST':
        return redirect(url_for('admin.manage_events'))
    return render_template('admin/edit_event.html')

@admin_bp.route('/events/delete')
def delete_event():
    return redirect(url_for('admin.manage_events'))