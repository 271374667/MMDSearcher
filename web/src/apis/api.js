import axios from 'axios';
// axios.defaults.baseURL = '';
axios.defaults.baseURL = '@/apis/xxx.json';

// 获取HomeMain中card的内容
export const getCardContent = () => axios.get('').then((res) => res.data);
