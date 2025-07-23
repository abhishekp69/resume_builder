// Main JavaScript for Resume Builder

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeFormHandlers();
    initializeTemplateGallery();
    initializeFormValidation();
    addAnimations();
});

function initializeFormHandlers() {
    // Handle template selection from gallery
    const templateCards = document.querySelectorAll('.template-card');
    templateCards.forEach(card => {
        card.addEventListener('click', function() {
            const templateId = this.dataset.templateId;
            if (templateId) {
                updateTemplateChoice(templateId);
            }
        });
    });

    // Auto-save form data to localStorage (if available)
    const formInputs = document.querySelectorAll('#resume-form input, #resume-form textarea, #resume-form select');
    formInputs.forEach(input => {
        input.addEventListener('input', debounce(saveFormData, 1000));
    });

    // Load saved form data
    loadFormData();
}

function initializeTemplateGallery() {
    // Add template preview functionality
    const templateCards = document.querySelectorAll('.template-card');
    templateCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

function initializeFormValidation() {
    const form = document.getElementById('resume-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            if (!validateForm()) {
                e.preventDefault();
                showAlert('Please fill in all required fields.', 'danger');
            }
        });
    }
}

function validateForm() {
    const requiredFields = document.querySelectorAll('#resume-form [required]');
    let isValid = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });

    return isValid;
}

function updateTemplateChoice(templateId) {
    const templateInput = document.getElementById('id_template_choice');
    if (templateInput) {
        templateInput.value = templateId;
        showAlert(`Template ${templateId} selected!`, 'success');
    }
}

function saveFormData() {
    if (typeof(Storage) !== "undefined") {
        const formData = new FormData(document.getElementById('resume-form'));
        const data = {};
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }
        localStorage.setItem('resumeFormData', JSON.stringify(data));
    }
}

function loadFormData() {
    if (typeof(Storage) !== "undefined") {
        const savedData = localStorage.getItem('resumeFormData');
        if (savedData) {
            const data = JSON.parse(savedData);
            Object.keys(data).forEach(key => {
                const field = document.querySelector(`[name="${key}"]`);
                if (field && !field.value) {
                    field.value = data[key];
                }
            });
        }
    }
}

function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('.container');
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    alertContainer.insertBefore(alert, alertContainer.firstChild);

    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (alert.parentNode) {
            alert.remove();
        }
    }, 5000);
}

function addAnimations() {
    // Add fade-in animations to elements
    const animatedElements = document.querySelectorAll('.card, .template-card');
    animatedElements.forEach((element, index) => {
        element.style.animationDelay = `${index * 0.1}s`;
        element.classList.add('fade-in');
    });
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// PDF download functionality
function downloadPDF(profileId) {
    showAlert('Generating PDF...', 'info');
    window.location.href = `/download/${profileId}/`;
}

// Template gallery search
function searchTemplates() {
    const searchInput = document.getElementById('template-search');
    const templateCards = document.querySelectorAll('.template-card');

    if (searchInput) {
        const searchTerm = searchInput.value.toLowerCase();

        templateCards.forEach(card => {
            const templateName = card.querySelector('.card-title').textContent.toLowerCase();
            if (templateName.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }
}

// Dynamic form management
function addFormsetForm(prefix) {
    const formset = document.getElementById(`${prefix}-formset`);
    const totalForms = document.getElementById(`id_${prefix}-TOTAL_FORMS`);
    const formCount = parseInt(totalForms.value);

    // Clone the last form
    const lastForm = formset.querySelector('.formset-form:last-child');
    const newForm = lastForm.cloneNode(true);

    // Update form indices
    const formRegex = new RegExp(`${prefix}-(\d+)-`, 'g');
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `${prefix}-${formCount}-`);

    // Clear form values
    const inputs = newForm.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        if (input.type !== 'hidden') {
            input.value = '';
        }
    });

    // Add to formset
    formset.appendChild(newForm);
    totalForms.value = formCount + 1;
}

// Export functions to global scope
window.downloadPDF = downloadPDF;
window.searchTemplates = searchTemplates;
window.addFormsetForm = addFormsetForm;