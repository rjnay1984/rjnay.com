import React, { useEffect } from 'react';

// import the useDispatch Redux hook
import { useDispatch, useSelector } from 'react-redux';		

// import our fetchRecipes thunk
import { fetchHomeContent, homeSelector } from './homeSlice';

function createMarkup(body) {
    return {__html: body }
}

export function Home() {
    const dispatch = useDispatch();
    const { loading, content, hasErrors } = useSelector(homeSelector);

    useEffect(() => {
        dispatch(fetchHomeContent())
    }, [dispatch])

    if (loading) return <div>Loading...</div>
    if (hasErrors) return <div>Error loading content.</div>

    return (
        <div>
            <h1>Home Page</h1>
            <div dangerouslySetInnerHTML={createMarkup(content.body)} />
        </div>
    );
}

