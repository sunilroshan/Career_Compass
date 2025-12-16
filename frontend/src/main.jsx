import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import CareerCompass from './CareerCompass.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* <App > */}
    <CareerCompass/>
  </StrictMode>,
)
