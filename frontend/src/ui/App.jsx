import React, { useEffect, useState } from 'react'
import axios from 'axios'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function CreativeCard({ ad }) {
  const firstAsset = ad.assets[0]
  return (
    <div style={{border:'1px solid #e2e2e2', borderRadius:8, padding:16, width:360, margin:12}}>
      <div style={{display:'flex', justifyContent:'space-between', marginBottom:8}}>
        <span style={{color: 'green', fontWeight: 600}}>{ad.status || 'Active'}</span>
        <span style={{opacity: .7}}>Library ID: {ad.library_id || '-'}</span>
      </div>
      <div style={{display:'flex', alignItems:'center', gap:8, marginBottom:8}}>
        <div style={{width:36, height:36, borderRadius:18, background:'#eee'}}></div>
        <div>
          <div style={{fontWeight:600}}>{ad.title || 'Sponsored Ad'}</div>
          <div style={{opacity:.7, fontSize:12}}>Sponsored</div>
        </div>
      </div>

      <div style={{margin:'8px 0', minHeight:200, display:'flex', alignItems:'center', justifyContent:'center', background:'#f8f8f8'}}>
        {firstAsset && firstAsset.type === 'video' ? (
          <video controls width="100%" src={firstAsset.preview_url}/>
        ) : (
          firstAsset ? <img src={firstAsset.preview_url} style={{maxWidth:'100%'}}/> : <div>No preview</div>
        )}
      </div>

      <div style={{opacity:.9, fontSize:14, marginBottom:8}}>{ad.body}</div>
      <div style={{display:'flex', justifyContent:'space-between'}}>
        <button onClick={() => window.alert('Details TBD')}>See ad details</button>
        {firstAsset && <a href={`${API}/assets/${firstAsset.id}/download`} target="_blank"><button>Download</button></a>}
      </div>
    </div>
  )
}

export default function App() {
  const [ads, setAds] = useState([])

  useEffect(() => {
    axios.get(`${API}/creatives`).then(r => setAds(r.data))
  }, [])

  return (
    <div style={{display:'flex'}}>
      <aside style={{width:280, borderRight:'1px solid #eee', padding:16}}>
        <div style={{fontWeight:700, marginBottom:12}}>Pages</div>
        <button onClick={() => window.alert('Add page — TBD')}>New page</button>
      </aside>
      <main style={{flex:1, padding:16}}>
        <div style={{display:'flex', flexWrap:'wrap'}}>
          {ads.map(ad => <CreativeCard key={ad.ad_id} ad={ad}/>)}
        </div>
      </main>
    </div>
  )
}
