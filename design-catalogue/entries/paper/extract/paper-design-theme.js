// React Theme — extracted from https://paper.design/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
    neutral900: string;
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '10': string;
    '11': string;
    '12': string;
    '13': string;
    '14': string;
    '17': string;
    '18': string;
    '22': string;
    '26': string;
    '36': string;
    '48': string;
    '64': string;
 *   };
 *   space: {
    '1': string;
    '28': string;
    '40': string;
    '48': string;
    '52': string;
    '60': string;
    '64': string;
    '80': string;
    '90': string;
    '96': string;
    '112': string;
    '120': string;
    '146': string;
    '154': string;
    '240': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
    md: string;
    xl: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#3d7cff",
    "secondary": "#0fa821",
    "accent": "#4d94fb",
    "background": "#f2f2f2",
    "foreground": "#222222",
    "neutral50": "#000000",
    "neutral100": "#1e2126",
    "neutral200": "#373a40",
    "neutral300": "#b7babf",
    "neutral400": "#585c62",
    "neutral500": "#82858b",
    "neutral600": "#797979",
    "neutral700": "#ebedef",
    "neutral800": "#959595",
    "neutral900": "#ffffff"
  },
  "fonts": {
    "body": "'Matter', sans-serif",
    "mono": "'Paper Mono', monospace"
  },
  "fontSizes": {
    "10": "10px",
    "11": "11px",
    "12": "12px",
    "13": "13px",
    "14": "14px",
    "17": "17px",
    "18": "18px",
    "22": "22px",
    "26": "26px",
    "36": "36px",
    "48": "48px",
    "64": "64px"
  },
  "space": {
    "1": "1px",
    "28": "28px",
    "40": "40px",
    "48": "48px",
    "52": "52px",
    "60": "60px",
    "64": "64px",
    "80": "80px",
    "90": "90px",
    "96": "96px",
    "112": "112px",
    "120": "120px",
    "146": "146px",
    "154": "154px",
    "240": "240px"
  },
  "radii": {
    "xs": "0px",
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "24px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgb(215, 215, 215) 0px 0px 0px 0.75px inset",
    "xs": "rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset",
    "md": "rgba(0, 0, 0, 0.08) 0px 8px 8px -4px, rgba(0, 0, 0, 0.08) 0px 2px 4px -2px, rgba(0, 0, 0, 0.08) 0px 1px 1px -1px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px",
    "xl": "rgba(0, 0, 0, 0.12) 0px 16px 32px -16px, rgba(0, 0, 0, 0.08) 0px 8px 16px -8px, rgba(0, 0, 0, 0.04) 0px 4px 8px -4px, rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#3d7cff",
      "light": "hsl(221, 100%, 77%)",
      "dark": "hsl(221, 100%, 47%)"
    },
    "secondary": {
      "main": "#0fa821",
      "light": "hsl(127, 84%, 51%)",
      "dark": "hsl(127, 84%, 21%)"
    },
    "background": {
      "default": "#f2f2f2",
      "paper": "#b7babf"
    },
    "text": {
      "primary": "#222222",
      "secondary": "#000000"
    }
  },
  "typography": {
    "fontFamily": "'Inter', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "570",
      "lineHeight": "36px"
    },
    "h2": {
      "fontSize": "26px",
      "fontWeight": "570",
      "lineHeight": "28px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "670",
      "lineHeight": "28px"
    },
    "body1": {
      "fontSize": "18px",
      "fontWeight": "400",
      "lineHeight": "28px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 1px 0px 0px",
    "rgba(128, 128, 128, 0.15) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 93px 26px 0px, rgba(0, 0, 0, 0.01) 0px 59px 24px 0px, rgba(0, 0, 0, 0.05) 0px 33px 20px 0px, rgba(0, 0, 0, 0.09) 0px 15px 15px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px",
    "rgb(216, 215, 216) 0px 0px 0px 0.75px inset",
    "rgb(215, 215, 215) 0px 0px 0px 0.75px inset",
    "rgba(255, 255, 255, 0.533) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.533) 0px 0px 1px 1px inset, rgba(0, 0, 0, 0.067) 0px 0.5px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 1px 0px, rgba(0, 0, 0, 0.133) 0px 0px 4px -1px"
  ]
};

export default theme;
