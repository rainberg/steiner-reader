import { Link } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';

export default function Recharge() {
  const packages = [
    { id: 1, credits: 100, price: '¥9.90', popular: false },
    { id: 2, credits: 500, price: '¥39.90', popular: true },
    { id: 3, credits: 1000, price: '¥69.90', popular: false },
    { id: 4, credits: 3000, price: '¥169.90', popular: false },
  ];

  return (
    <div className="min-h-screen pt-24 pb-16">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/profile"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回
        </Link>

        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2 font-['Playfair_Display']">
            充值积分
          </h1>
          <p className="text-gray-600">获取更多积分，体验完整翻译功能</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {packages.map((pkg) => (
          <button
            key={pkg.id}
            className={`relative p-6 rounded-2xl border-2 transition-all ${
              pkg.popular
                ? 'border-[#1e3a8a] bg-[#1e3a8a]/5'
                : 'border-gray-200 hover:border-[#1e3a8a]/30 hover:bg-[#1e3a8a]/5'
            }`}
          >
            {pkg.popular && (
              <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                <span className="bg-[#d4a574] text-white text-xs px-3 py-1 rounded-full">
                  推荐
                </span>
              </div>
            )}
            <div className="text-center">
              <div className="text-3xl font-bold text-[#1e3a8a] mb-2">
                {pkg.credits}
              </div>
              <div className="text-sm text-gray-500 mb-4">积分</div>
              <div className="text-2xl font-bold text-gray-900">
                {pkg.price}
              </div>
            </div>
          </button>
          ))}
        </div>

        <div className="mt-8">
          <button className="w-full py-4 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors">
            立即充值
          </button>
        </div>
      </div>
    </div>
  );
}
