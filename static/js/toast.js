function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    if (type === 'success') {
        toastComponent.classList.add('bg-yellow-200', 'border-yellow-800', 'text-blue-600');
        toastComponent.style.border = '3px solid #ffcc00ff';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-100', 'border-red-600', 'text-red-800');
        toastComponent.style.border = '1px solid #dc2626';
    } else {
        toastComponent.classList.add('bg-blue-100', 'border-blue-500', 'text-blue-800');
        toastComponent.style.border = '1px solid #3b82f6';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-x-64');
    toastComponent.classList.add('opacity-100', 'translate-x-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-x-0');
        toastComponent.classList.add('opacity-0', 'translate-x-64');
    }, duration);
}