import React from 'react';

const DeleteAccount = () => {
    const handleDelete = async () => {
        // handle account deletion
    };

    return (
        <div>
            <h1>Delete Account</h1>
            <button onClick={handleDelete}>Confirm Delete</button>
        </div>
    );
}

export default DeleteAccount;
