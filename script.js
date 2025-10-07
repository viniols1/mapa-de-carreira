document.addEventListener('DOMContentLoaded', () => {

    const mapContainer = document.getElementById('career-map');
    const detailsSidebar = document.getElementById('details-sidebar');
    const detailsTitle = document.getElementById('details-title');
    const detailsDescription = document.getElementById('details-description');
    const hardSkillsList = document.getElementById('hard-skills-list');
    const softSkillsList = document.getElementById('soft-skills-list');
    const trackSelector = document.getElementById('track-selector');
    const trackDescription = document.getElementById('track-description');

    let allTracksData = null;
    let currentTrack = null;  
    let allNodes = [];

    async function loadCareerData() {
        try {
            const response = await fetch('career_path.json');
            allTracksData = await response.json();
            
            
            populateTrackSelector();

            renderTrack(allTracksData[0].trackId);

        } catch (error) {
            console.error('Erro ao carregar os dados da carreira:', error);
        }
    }

    
    function populateTrackSelector() {
        if (!allTracksData) return;

        allTracksData.forEach(track => {
            const option = document.createElement('option');
            option.value = track.trackId;
            option.textContent = track.trackName;
            trackSelector.appendChild(option);
        });

        
        trackSelector.addEventListener('change', (event) => {
            renderTrack(event.target.value);
        });
    }

    
    function renderTrack(trackId) {
        
        currentTrack = allTracksData.find(track => track.trackId === trackId);
        if (!currentTrack) return;

        
        mapContainer.innerHTML = '';
        allNodes = [];
        detailsSidebar.classList.add('sidebar-hidden');
        trackDescription.textContent = currentTrack.trackDescription; 

        
        currentTrack.nodes.forEach(nodeData => {
            const nodeElement = document.createElement('div');
            nodeElement.classList.add('career-node');
            nodeElement.textContent = nodeData.label;
            nodeElement.dataset.id = nodeData.id;

            mapContainer.appendChild(nodeElement);
            allNodes.push(nodeElement);

            nodeElement.addEventListener('click', () => onNodeClick(nodeData.id));
        });
    }
    
    
    function onNodeClick(nodeId) {
        if (!currentTrack) return;

        const clickedNodeData = currentTrack.nodes.find(n => n.id === nodeId);
        if (!clickedNodeData) return;

        detailsSidebar.classList.remove('sidebar-hidden');
        detailsTitle.textContent = clickedNodeData.label;
        detailsDescription.textContent = clickedNodeData.description;

        hardSkillsList.innerHTML = '';
        softSkillsList.innerHTML = '';

        clickedNodeData.skills.hard.forEach(skill => {
            const li = document.createElement('li');
            li.textContent = skill;
            hardSkillsList.appendChild(li);
        });

        clickedNodeData.skills.soft.forEach(skill => {
            const li = document.createElement('li');
            li.textContent = skill;
            softSkillsList.appendChild(li);
        });

        allNodes.forEach(node => {
            node.classList.remove('active', 'next-step');
        });

        const clickedNodeElement = allNodes.find(node => node.dataset.id === nodeId);
        clickedNodeElement.classList.add('active');

        
        const nextStepIds = currentTrack.edges
            .filter(edge => edge.from === nodeId)
            .map(edge => edge.to);

        nextStepIds.forEach(id => {
            const nextStepNode = allNodes.find(node => node.dataset.id === id);
            if (nextStepNode) {
                nextStepNode.classList.add('next-step');
            }
        });
    }

    loadCareerData();

});
