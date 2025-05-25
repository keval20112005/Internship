import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function Logout() {
    const navigate = useNavigate();

    useEffect(() => {
        localStorage.removeItem('token'); 
        alert('You have been logged out');
        navigate('/'); 
    }, [navigate]);

    return null; 
}
